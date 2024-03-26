namespace ACR_Phantom_GUI
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.MainTabControl = new System.Windows.Forms.TabControl();
            this.StartPage = new System.Windows.Forms.TabPage();
            this.SNRResults = new System.Windows.Forms.TabPage();
            this.GeometricAccuracy = new System.Windows.Forms.TabPage();
            this.StartButton = new System.Windows.Forms.Button();
            this.DCMPath = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.OuputPath = new System.Windows.Forms.TextBox();
            this.LogBoxField = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.MainTabControl.SuspendLayout();
            this.StartPage.SuspendLayout();
            this.SuspendLayout();
            // 
            // MainTabControl
            // 
            this.MainTabControl.Controls.Add(this.StartPage);
            this.MainTabControl.Controls.Add(this.SNRResults);
            this.MainTabControl.Controls.Add(this.GeometricAccuracy);
            this.MainTabControl.Dock = System.Windows.Forms.DockStyle.Fill;
            this.MainTabControl.Location = new System.Drawing.Point(0, 0);
            this.MainTabControl.Name = "MainTabControl";
            this.MainTabControl.SelectedIndex = 0;
            this.MainTabControl.Size = new System.Drawing.Size(1058, 598);
            this.MainTabControl.TabIndex = 0;
            // 
            // StartPage
            // 
            this.StartPage.Controls.Add(this.label3);
            this.StartPage.Controls.Add(this.LogBoxField);
            this.StartPage.Controls.Add(this.label2);
            this.StartPage.Controls.Add(this.OuputPath);
            this.StartPage.Controls.Add(this.label1);
            this.StartPage.Controls.Add(this.DCMPath);
            this.StartPage.Controls.Add(this.StartButton);
            this.StartPage.Location = new System.Drawing.Point(4, 22);
            this.StartPage.Name = "StartPage";
            this.StartPage.Padding = new System.Windows.Forms.Padding(3);
            this.StartPage.Size = new System.Drawing.Size(1050, 572);
            this.StartPage.TabIndex = 0;
            this.StartPage.Text = "Start Page";
            this.StartPage.UseVisualStyleBackColor = true;
            // 
            // SNRResults
            // 
            this.SNRResults.Location = new System.Drawing.Point(4, 22);
            this.SNRResults.Name = "SNRResults";
            this.SNRResults.Padding = new System.Windows.Forms.Padding(3);
            this.SNRResults.Size = new System.Drawing.Size(1050, 572);
            this.SNRResults.TabIndex = 1;
            this.SNRResults.Text = "SNR Results";
            this.SNRResults.UseVisualStyleBackColor = true;
            // 
            // GeometricAccuracy
            // 
            this.GeometricAccuracy.Location = new System.Drawing.Point(4, 22);
            this.GeometricAccuracy.Name = "GeometricAccuracy";
            this.GeometricAccuracy.Size = new System.Drawing.Size(1050, 572);
            this.GeometricAccuracy.TabIndex = 2;
            this.GeometricAccuracy.Text = "Geometric Accuracy";
            this.GeometricAccuracy.UseVisualStyleBackColor = true;
            // 
            // StartButton
            // 
            this.StartButton.Location = new System.Drawing.Point(8, 526);
            this.StartButton.Name = "StartButton";
            this.StartButton.Size = new System.Drawing.Size(117, 23);
            this.StartButton.TabIndex = 0;
            this.StartButton.Text = "Start Analysis";
            this.StartButton.UseVisualStyleBackColor = true;
            this.StartButton.Click += new System.EventHandler(this.StartButton_Click);
            // 
            // DCMPath
            // 
            this.DCMPath.Location = new System.Drawing.Point(81, 13);
            this.DCMPath.Name = "DCMPath";
            this.DCMPath.Size = new System.Drawing.Size(465, 20);
            this.DCMPath.TabIndex = 1;
            this.DCMPath.Text = "D:/Hazen-ScottishACR-Fork/MedACRTesting/ACR_ARDL_Tests";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(8, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(67, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "DICOM Path";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(8, 42);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(67, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "Results Path";
            // 
            // OuputPath
            // 
            this.OuputPath.Location = new System.Drawing.Point(81, 39);
            this.OuputPath.Name = "OuputPath";
            this.OuputPath.Size = new System.Drawing.Size(465, 20);
            this.OuputPath.TabIndex = 3;
            this.OuputPath.Text = "C:/Users/John/Desktop/DockerLocalTest/ACRResults";
            // 
            // LogBoxField
            // 
            this.LogBoxField.Location = new System.Drawing.Point(157, 415);
            this.LogBoxField.Multiline = true;
            this.LogBoxField.Name = "LogBoxField";
            this.LogBoxField.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.LogBoxField.Size = new System.Drawing.Size(887, 151);
            this.LogBoxField.TabIndex = 5;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(154, 399);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(25, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Log";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1058, 598);
            this.Controls.Add(this.MainTabControl);
            this.Name = "Form1";
            this.Text = "Form1";
            this.MainTabControl.ResumeLayout(false);
            this.StartPage.ResumeLayout(false);
            this.StartPage.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl MainTabControl;
        private System.Windows.Forms.TabPage StartPage;
        private System.Windows.Forms.TabPage SNRResults;
        private System.Windows.Forms.TabPage GeometricAccuracy;
        private System.Windows.Forms.Button StartButton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox LogBoxField;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox OuputPath;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox DCMPath;
    }
}

