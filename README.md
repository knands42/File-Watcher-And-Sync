# FileWatcherAndSync

Just a simple script to listen changes on my directory and sync it to my remote server.
> This should work for many scenarios, but my main goal was to sync my emulators savestates and memstates sync with my backup server.

For now I just implemented a connection with a smb server, but eventually is going to have NFS client as well.

### Setup

Clone this project into a directory available in your path.

```bash
git clone git@github.com:caiofernandes00/File-Watcher-And-Sync.git /opt/File-Watcher-And-Sync
cd /opt/File-Watcher-And-Sync
pip install -r requirements.txt
chmod +x exec.sh
export PATH=$PATH:$/opt/File-Watcher-And-Sync
```

*Just for now* it doesn't have *yet* any way to create a config file dynamically, but it will be improved in the future.
So for the first setup you need to create a config file called `.env` and the content should be followed by the same as the `.env.example` file.

### Execute

Once the previous step is completed, you can execute the script.

```bash
watch_and_send
```
