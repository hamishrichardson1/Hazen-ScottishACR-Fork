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
            this.label3 = new System.Windows.Forms.Label();
            this.LogBoxField = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.OuputPath = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.StartButton = new System.Windows.Forms.Button();
            this.DCMPath = new System.Windows.Forms.TextBox();
            this.ShowAllOutput = new System.Windows.Forms.CheckBox();
            this.SeqSelector = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.ResultsTable = new System.Windows.Forms.DataGridView();
            this.TestCol = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ToleranceCol = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ResultCol = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.PassedCol = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.ResultsTable)).BeginInit();
            this.SuspendLayout();
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(189, 221);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(25, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Log";
            // 
            // LogBoxField
            // 
            this.LogBoxField.Location = new System.Drawing.Point(185, 244);
            this.LogBoxField.Multiline = true;
            this.LogBoxField.Name = "LogBoxField";
            this.LogBoxField.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.LogBoxField.Size = new System.Drawing.Size(861, 101);
            this.LogBoxField.TabIndex = 5;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 38);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(67, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "Results Path";
            // 
            // OuputPath
            // 
            this.OuputPath.Location = new System.Drawing.Point(95, 35);
            this.OuputPath.Name = "OuputPath";
            this.OuputPath.ReadOnly = true;
            this.OuputPath.Size = new System.Drawing.Size(465, 20);
            this.OuputPath.TabIndex = 3;
            this.OuputPath.Text = "C:/Users/John/Desktop/DockerLocalTest/ACRResults";
            this.OuputPath.MouseClick += new System.Windows.Forms.MouseEventHandler(this.OutputPath_click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 12);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(67, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "DICOM Path";
            // 
            // StartButton
            // 
            this.StartButton.Location = new System.Drawing.Point(30, 322);
            this.StartButton.Name = "StartButton";
            this.StartButton.Size = new System.Drawing.Size(117, 23);
            this.StartButton.TabIndex = 0;
            this.StartButton.Text = "Start Analysis";
            this.StartButton.UseVisualStyleBackColor = true;
            this.StartButton.Click += new System.EventHandler(this.StartButton_Click);
            // 
            // DCMPath
            // 
            this.DCMPath.Location = new System.Drawing.Point(95, 9);
            this.DCMPath.Name = "DCMPath";
            this.DCMPath.ReadOnly = true;
            this.DCMPath.Size = new System.Drawing.Size(465, 20);
            this.DCMPath.TabIndex = 1;
            this.DCMPath.Text = "D:/Hazen-ScottishACR-Fork/MedACRTesting/ACR_ARDL_Tests";
            this.DCMPath.MouseClick += new System.Windows.Forms.MouseEventHandler(this.DCMPath_click);
            this.DCMPath.TextChanged += new System.EventHandler(this.DCMPath_TextChanged);
            // 
            // ShowAllOutput
            // 
            this.ShowAllOutput.AutoSize = true;
            this.ShowAllOutput.Location = new System.Drawing.Point(220, 221);
            this.ShowAllOutput.Name = "ShowAllOutput";
            this.ShowAllOutput.Size = new System.Drawing.Size(102, 17);
            this.ShowAllOutput.TabIndex = 7;
            this.ShowAllOutput.Text = "Show All Output";
            this.ShowAllOutput.UseVisualStyleBackColor = true;
            // 
            // SeqSelector
            // 
            this.SeqSelector.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.SeqSelector.FormattingEnabled = true;
            this.SeqSelector.Location = new System.Drawing.Point(586, 34);
            this.SeqSelector.Name = "SeqSelector";
            this.SeqSelector.Size = new System.Drawing.Size(460, 21);
            this.SeqSelector.TabIndex = 8;
            this.SeqSelector.SelectedIndexChanged += new System.EventHandler(this.SeqSelector_SelectedIndexChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(586, 16);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(103, 13);
            this.label4.TabIndex = 9;
            this.label4.Text = "Sequence Selection";
            // 
            // ResultsTable
            // 
            this.ResultsTable.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.ResultsTable.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.TestCol,
            this.ToleranceCol,
            this.ResultCol,
            this.PassedCol});
            this.ResultsTable.Location = new System.Drawing.Point(328, 61);
            this.ResultsTable.Name = "ResultsTable";
            this.ResultsTable.ReadOnly = true;
            this.ResultsTable.RowHeadersVisible = false;
            this.ResultsTable.Size = new System.Drawing.Size(718, 170);
            this.ResultsTable.TabIndex = 10;
            // 
            // TestCol
            // 
            this.TestCol.HeaderText = "Test";
            this.TestCol.Name = "TestCol";
            this.TestCol.ReadOnly = true;
            // 
            // ToleranceCol
            // 
            this.ToleranceCol.HeaderText = "Tolerance";
            this.ToleranceCol.Name = "ToleranceCol";
            this.ToleranceCol.ReadOnly = true;
            // 
            // ResultCol
            // 
            this.ResultCol.HeaderText = "Result";
            this.ResultCol.Name = "ResultCol";
            this.ResultCol.ReadOnly = true;
            // 
            // PassedCol
            // 
            this.PassedCol.HeaderText = "Passed?";
            this.PassedCol.Name = "PassedCol";
            this.PassedCol.ReadOnly = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1058, 357);
            this.Controls.Add(this.ResultsTable);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.SeqSelector);
            this.Controls.Add(this.ShowAllOutput);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.LogBoxField);
            this.Controls.Add(this.DCMPath);
            this.Controls.Add(this.StartButton);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.OuputPath);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.ResultsTable)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Button StartButton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox LogBoxField;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox OuputPath;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox DCMPath;
        private System.Windows.Forms.CheckBox ShowAllOutput;
        private System.Windows.Forms.ComboBox SeqSelector;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.DataGridView ResultsTable;
        private System.Windows.Forms.DataGridViewTextBoxColumn TestCol;
        private System.Windows.Forms.DataGridViewTextBoxColumn ToleranceCol;
        private System.Windows.Forms.DataGridViewTextBoxColumn ResultCol;
        private System.Windows.Forms.DataGridViewTextBoxColumn PassedCol;
    }
}

