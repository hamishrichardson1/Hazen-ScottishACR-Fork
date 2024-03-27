using EvilDICOM.Core;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using EvilDICOM;
using EvilDICOM.Core.Helpers;
using System.IO;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;
using FellowOakDicom;

namespace ACR_Phantom_GUI
{
    public partial class Form1 : Form
    {
        private BackgroundWorker Worker;
        public Form1()
        {
            try
            {
                InitializeComponent();
                Worker = new BackgroundWorker();
                Worker.DoWork += Worker_DoWork;
                Worker.ProgressChanged += Worker_ProgressChanged;
                Worker.RunWorkerCompleted += Worker_RunWorkerCompleted;
                Worker.WorkerReportsProgress = true;
                Worker.WorkerSupportsCancellation = true;
                UpdateSequences();
            }
            catch (Exception ex) { MessageBox.Show(ex.Message); }
        }

        private void UpdateSequences()
        {
            try
            {
                if (DCMPath.Text.Length > 0)
                {
                    SeqSelector.Items.Clear();
                    List<string> filePaths = Directory.GetFiles(DCMPath.Text, "*", SearchOption.TopDirectoryOnly).ToList();
                    List<string> seq = new List<string>();
                    foreach (string DCMPath in filePaths)
                    {
                        bool isDicom = DicomFile.HasValidHeader(DCMPath);
                        if (isDicom==true)
                        {
                            DICOMObject DCM = DICOMObject.Read(DCMPath);
                            string Sequence = DCM.FindFirst(TagHelper.SeriesDescription).DData.ToString();
                            seq.Add(Sequence);
                        }
                    }
                    SeqSelector.Items.AddRange(seq.Distinct().ToArray());
                    if (SeqSelector.Items.Count > 0) { SeqSelector.SelectedIndex = 0; }
                }
            }
            catch (Exception ex) { MessageBox.Show(ex.Message); }
        }

        private void SeqSelector_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            try
            {
                StartButton.Enabled = false;
                SeqSelector.Enabled = false;
                Worker.RunWorkerAsync();
            }
            catch (Exception ex){MessageBox.Show(ex.Message);}
        }

        private void Worker_DoWork(object sender, System.ComponentModel.DoWorkEventArgs e)
        {
            try
            {
                //Run the docker image
                string DCMFolder = null;
                DCMPath.Invoke(new MethodInvoker(delegate { DCMFolder = DCMPath.Text; }));
                string OutputFolder = null;
                OuputPath.Invoke(new MethodInvoker(delegate { OutputFolder = OuputPath.Text; }));
                string Sequence = null;
                SeqSelector.Invoke(new MethodInvoker(delegate { Sequence = SeqSelector.Text; }));

                var processInfo = new ProcessStartInfo("docker", $"run -v " + DCMFolder + ":/app/DataTransfer -v" + OutputFolder + ":/app/OutputFolder -v C:/Users/John/Desktop/DockerLocalTest/ToleranceTable:/app/ToleranceTable docker-acr-phantom -seq \"" + Sequence + "\" -RunAll");
                processInfo.CreateNoWindow = true;
                processInfo.UseShellExecute = false;
                processInfo.RedirectStandardOutput = true;
                processInfo.RedirectStandardError = true;
                int exitCode;
                using (var process = new Process())
                {
                    process.StartInfo = processInfo;
                    process.OutputDataReceived += new DataReceivedEventHandler(OutputHandler);
                    process.ErrorDataReceived += new DataReceivedEventHandler(OutputHandler);

                    process.Start();
                    process.BeginOutputReadLine();
                    process.BeginErrorReadLine();
                    process.WaitForExit(1200000);
                    if (!process.HasExited)
                    {
                        process.Kill();
                    }

                    exitCode = process.ExitCode;
                    process.Close();
                }

                //Prune the container we just made
                processInfo = new ProcessStartInfo("docker", $"container prune -f");
                processInfo.CreateNoWindow = true;
                processInfo.UseShellExecute = false;
                processInfo.RedirectStandardOutput = true;
                processInfo.RedirectStandardError = true;
                using (var process = new Process())
                {
                    process.StartInfo = processInfo;
                    process.OutputDataReceived += new DataReceivedEventHandler(OutputHandler);
                    process.ErrorDataReceived += new DataReceivedEventHandler(OutputHandler);
                    process.Start();
                    process.BeginOutputReadLine();
                    process.BeginErrorReadLine();
                    process.WaitForExit(1200000);
                    if (!process.HasExited)
                    {
                        process.Kill();
                    }

                    exitCode = process.ExitCode;
                    process.Close();
                }
            }
            catch (Exception ex) { MessageBox.Show(ex.Message); }


        }
        void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            try
            {
                bool OutputAll = false;
                string Line = "";
                LogBoxField.Invoke(new MethodInvoker(delegate { OutputAll = ShowAllOutput.Checked; }));
                LogBoxField.Invoke(new MethodInvoker(delegate { Line = outLine.Data + Environment.NewLine;}));

                if (OutputAll == true || OutputAll == false)
                {
                    LogBoxField.Invoke(new MethodInvoker(delegate { LogBoxField.Text += Line; LogBoxField.SelectionStart = LogBoxField.Text.Length; LogBoxField.ScrollToCaret(); }));
                }
            }
            catch(Exception ex) { MessageBox.Show(ex.Message);}
        }
        
        private void Worker_ProgressChanged(object sender, System.ComponentModel.ProgressChangedEventArgs e)
        {
            try
            {

            }
            catch(Exception ex) { MessageBox.Show(ex.Message);}
        }
        private void Worker_RunWorkerCompleted(object sender, System.ComponentModel.RunWorkerCompletedEventArgs e)
        {
            try
            {
                LogBoxField.Text += "Finished" + Environment.NewLine;
                StartButton.Enabled = true;
                SeqSelector.Enabled = true;
                LogBoxField.SelectionStart = LogBoxField.Text.Length;
                LogBoxField.ScrollToCaret();
            }
            catch(Exception ex) { MessageBox.Show(ex.Message);}
        }

        private void DCMPath_TextChanged(object sender, EventArgs e)
        {
            //TODO
        }

        private void DCMPath_click(object sender, MouseEventArgs e)
        {
            using (var fbd = new FolderBrowserDialog())
            {
                DialogResult result = fbd.ShowDialog();
                DCMPath.Text = fbd.SelectedPath;
                if (result == DialogResult.OK)
                {
                    UpdateSequences();
                }
            }

        }

        private void OutputPath_click(object sender, MouseEventArgs e)
        {
            using (var fbd = new FolderBrowserDialog())
            {
                DialogResult result = fbd.ShowDialog();
                OuputPath.Text = fbd.SelectedPath;
            }
        }
    }
}
