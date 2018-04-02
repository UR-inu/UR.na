import Tkinter as tk
import os
import stat
import sys

class ExampleApp(tk.Frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=500,
                          height=200)
        # Set the title
        self.master.title('UR Manager')
 
        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        self.pack()
 
        
        # Use a StringVar to access the selector's value
        self.greeting_var = tk.StringVar()
        self.greeting = tk.OptionMenu(self,
                                      self.greeting_var,
                                      'Backup Programs',
                                      'Backup Logfiles',
                                      'Backup Configuration Files')
        self.greeting_var.set('Select an Action')

		

 
        # The recipient text entry control and its StringVar
        self.recipient_var = tk.StringVar()
        self.recipient = tk.Entry(self,
                                  textvariable=self.recipient_var)
        self.recipient_var.set('Enter IP Address')

 
        # The go button
        self.go_button = tk.Button(self,
                                   text='Go',
                                   command=self.print_out)
								   
 
        # Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.recipient.pack(fill=tk.X, side=tk.TOP)

    def print_out(self):
        ''' Print a greeting constructed
            from the selections made by
            the user. '''
        print('%s, %s!' % (self.greeting_var.get().title(),
                           self.recipient_var.get()))
	print (self.recipient_var)
	if self.greeting_var.get() == 'Backup Logfiles':
		import paramiko
		#this section of code establishes a SSH connection to the robot, switches to the /root/.ssh folder
		#and list its contents
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		target_host = self.recipient_var.get()
		target_port = 22
		pwd = 'easybot'
		un = 'root'
		ssh.connect( hostname = target_host , username = un, password = pwd )
		stdin, stdout, stderr = ssh.exec_command('ls -1 /root/.ssh|head -n 5')
		print "STDOUT:\n%s\n\nSTDERR:\n%s\n" %( stdout.read(), stderr.read() )
		# this section of code is copying a file from the local PC to transfer to robot
		sftp = ssh.open_sftp()
		file_local = 'c:\Python27\urmagic_log_file.sh'
		file_remote = '/root/.ssh/urmagic_log_file.sh'
		print file_local + '>>>>' + file_remote
		sftp.put(file_local, file_remote)
		sftp.chmod("/root/.ssh/urmagic_log_file.sh", 777)
		ssh.exec_command("/root/.ssh/urmagic_log_file.sh")
		sftp.close()
		ssh.close()
	if self.greeting_var.get() == 'Backup Programs':
		import paramiko
		#this section of code establishes a SSH connection to the robot, switches to the /root/.ssh folder
		#and list its contents
		ssh = paramiko.SSHClient()
		#lp = paramiko.sftp_client.SFTPClient()
		
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		target_host = self.recipient_var.get()
		target_port = 22
		pwd = 'easybot'
		un = 'root'
		ssh.connect( hostname = target_host , username = un, password = pwd )
		stdin, stdout, stderr = ssh.exec_command('ls -1 /root/.ssh|head -n 5')
		print "STDOUT:\n%s\n\nSTDERR:\n%s\n" %( stdout.read(), stderr.read() )
		# this section of code is copying a file from the local PC to transfer to robot
		sftp = ssh.open_sftp()
		stdin, stdout, stderr = ssh.exec_command('head -1 /root/ur-serial')
		serialNum = "STDOUT:\n%s\n\nSTDERR:\n%s\n" %( stdout.read(), stderr.read() )
		print (serialNum)
		
		file_local = 'c:\Python27\urmagic_backup_programs_mod.sh'
		file_remote = '/root/.ssh/backup_programs.sh'
		print file_local + '>>>>' + file_remote
		sftp.put(file_local, file_remote)
		#ef write_command(self,text,remotefile):
		sftp.chmod("/root/.ssh/backup_programs.sh", 777)
		ssh.exec_command("/root/.ssh/backup_programs.sh")
		
		#backup_file = '/root/serialNum'
		#Transfer_backup = 'c:\Python27\serialNum'
		#sftp.get(backup_file,Transfer_backup)
		sftp.close()
		ssh.close()
	if self.greeting_var.get() == 'Backup Configuration Files':
		import paramiko
		#this section of code establishes a SSH connection to the robot, switches to the /root/.ssh folder
		#and list its contents
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		target_host = self.recipient_var.get()
		target_port = 22
		pwd = 'easybot'
		un = 'root'
		ssh.connect( hostname = target_host , username = un, password = pwd )
		stdin, stdout, stderr = ssh.exec_command('ls -1 /root/.ssh|head -n 5')
		print "STDOUT:\n%s\n\nSTDERR:\n%s\n" %( stdout.read(), stderr.read() )
		# this section of code is copying a file from the local PC to transfer to robot
		sftp = ssh.open_sftp()
		file_local = 'c:\Python27\urmagic_configuration_files.sh'
		file_remote = '/root/.ssh/configuration_file.sh'
		print file_local + '>>>>' + file_remote
		sftp.put(file_local, file_remote)
		sftp.chmod("/root/.ssh/configuration_file.sh", 777)
		ssh.exec_command("/root/.ssh/configuration_file.sh")
		sftp.close()
		ssh.close()
    def run(self):
        ''' Run the app '''
        self.mainloop()
		

	
app = ExampleApp(tk.Tk())
app.run()
	
