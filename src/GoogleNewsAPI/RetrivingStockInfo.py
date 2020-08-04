import sys
sys.path.insert(1, 'D:\Sync\Advanced Database Topics\FinalProject\Max Repo\ADTFinalProject\src\MongoDBAtlasAPI')

from MongoDBAtlasAPIAuthentication import MongoDBAtlasAPIAuthentication

if __name__ == "__main__":
    mdbaa = MongoDBAtlasAPIAuthentication()
    client = mdbaa.get_mongodb_client()
    # print client state
    print(client.state)