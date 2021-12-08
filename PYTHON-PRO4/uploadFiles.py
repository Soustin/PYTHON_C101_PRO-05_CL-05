import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for roots, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    access_token = 'sl.A9yNYREMqmszJShP2kVwWYXigneg2qfSsfN-vt6GLFqpKXM_3HEl1pQAuhK0TcwM1OydQiqCIpwkiirxTdAcXk6BDFSv56cYkk7YfDjEiu-p83-Zw5zdBq9XHeH5IqfKEK__njHXcqFW'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
