
import os
import shutil
import time

def main():

	delFoldersCount  = 0
	delFilesCount = 0

	path = input("Enter Path to Check ")

	days = 30

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):

		for root_folder, folders, files in os.walk(path):

			if seconds >= get_file_or_folder_age(root_folder):

				remove_folder(root_folder)
				delFoldersCount  += 1

				break

			else:

				for folder in folders:

					folder_path = os.path.join(root_folder, folder)

					if seconds >= get_file_or_folder_age(folder_path):

						remove_folder(folder_path)
						delFoldersCount  += 1

				for f in files:

					file_path = os.path.join(root_folder, f)

					if seconds >= get_file_or_folder_age(file_path):

						remove_file(file_path)
						delFilesCount += 1 

		else:

			if seconds >= get_file_or_folder_age(path):

				remove_file(path)
				delFilesCount += 1 

	else:

		print(f'"{path}" is not found')
		delFilesCount += 1 

	print(f"Total folders deleted: {delFoldersCount }")
	print(f"Total files deleted: {delFilesCount }")


def remove_folder(path):

	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		print(f"Unable to delete the folder: "+path)



def remove_file(path):

	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the file: "+path)


def get_file_or_folder_age(path):

	currentTime = os.stat(path).st_ctime

	return currentTime


if __name__ == '__main__':
	main()