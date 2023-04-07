import sys
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

file_name = sys.argv[3]

def get_sharepoint_context_using_user():
    username = sys.argv[1]
    password = sys.argv[2]
    sharepoint_url = 'https://mahamalage.sharepoint.com'
    user_credentials = UserCredential(username,password)
    context = ClientContext(sharepoint_url).with_credentials(user_credentials)
    return context


def create_sharepoint_directory(dir_name: str):
    if dir_name:
        context = get_sharepoint_context_using_user()
        result = context.web.folders.add(f'Shared Documents/{dir_name}').execute_query()
        if result:
            # documents is titled as Shared Documents for relative URL in SP
            relative_url = f'Shared Documents/{dir_name}'
            return relative_url


def upload_to_sharepoint(dir_name: str, file_name: str):
    sp_relative_url = create_sharepoint_directory(dir_name)
    context = get_sharepoint_context_using_user()
    target_folder = context.web.get_folder_by_server_relative_url(sp_relative_url)
    with open(f'uploads/{file_name}', 'rb') as content_file:
        file_content = content_file.read()
        target_folder.upload_file(file_name, file_content).execute_query()


#create_sharepoint_directory('test directory')

upload_to_sharepoint("DMKK", file_name)

