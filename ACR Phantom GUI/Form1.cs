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

namespace ACR_Phantom_GUI
{
    public partial class Form1 : Form
    {
        private BackgroundWorker Worker;
        public Form1()
        {
            InitializeComponent();
            /*
            foreach (TabPage tab in MainTabControl.TabPages)
            {
                tab.Enabled = false;
            }
            (MainTabControl.TabPages[0] as TabPage).Enabled = true;
            */
            Worker = new BackgroundWorker();
            Worker.DoWork += Worker_DoWork;
            Worker.ProgressChanged += Worker_ProgressChanged;
            Worker.RunWorkerCompleted += Worker_RunWorkerCompleted;
            Worker.WorkerReportsProgress = true;
            Worker.WorkerSupportsCancellation = true;


        }

        private void UpdateDICOMSequences()
        {
            DICOMObject DCM = DICOMObject.Read("D:\\Hazen-ScottishACR-Fork\\MedACRTesting\\ACR_ARDL_Tests\\MR.X.1.2.276.0.7230010.3.1.4.0.1432.1707426038.710703.dcm");
            string Sequence = DCM.FindFirst(TagHelper.SeriesDescription).DData.ToString();

        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            StartButton.Enabled = false;
            Worker.RunWorkerAsync();
        }

        private void Worker_DoWork(object sender, System.ComponentModel.DoWorkEventArgs e)
        {
            //Run the docker image
            string DCMFolder = null;
            if (DCMPath.InvokeRequired)
            {
                DCMPath.Invoke(new MethodInvoker(delegate { DCMFolder = DCMPath.Text; }));
            }
            string OutputFolder = null;
            if (OuputPath.InvokeRequired)
            {
                OuputPath.Invoke(new MethodInvoker(delegate { OutputFolder = OuputPath.Text; }));
            }

            string Sequence = "ACR AxT1 High AR";

            var processInfo = new ProcessStartInfo("docker", $"run -v "+DCMFolder+":/app/DataTransfer -v"+OutputFolder+":/app/OutputFolder -v C:/Users/John/Desktop/DockerLocalTest/ToleranceTable:/app/ToleranceTable docker-acr-phantom -seq \""+Sequence+"\" -RunAll");
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
        void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            //* Do your stuff with the output (write to console/log/StringBuilder)
            //Console.WriteLine(outLine.Data);


            if (LogBoxField.InvokeRequired)
            {
                LogBoxField.Invoke(new MethodInvoker(delegate { LogBoxField.Text += outLine.Data + Environment.NewLine; LogBoxField.SelectionStart = LogBoxField.Text.Length; LogBoxField.ScrollToCaret(); }));
            }
        }
        
        private void Worker_ProgressChanged(object sender, System.ComponentModel.ProgressChangedEventArgs e)
        {
        }
        private void Worker_RunWorkerCompleted(object sender, System.ComponentModel.RunWorkerCompletedEventArgs e)
        {
            LogBoxField.Text += "Finished" + Environment.NewLine;
            StartButton.Enabled = true;
            LogBoxField.SelectionStart = LogBoxField.Text.Length; 
            LogBoxField.ScrollToCaret();
        }
    }
}
