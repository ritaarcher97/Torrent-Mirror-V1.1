export MAX_DOWNLOAD_SPEED=0
tracker_list=$(curl -Ns https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all_aria2.txt https://ngosang.github.io/trackerslist/trackers_all_http.txt https://newtrackon.com/api/all https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all.txt | awk '$0' | tr '\n\n' ',')
export MAX_CONCURRENT_DOWNLOADS=7

aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port 6800 --check-certificate=false \
--max-connection-per-server=10 --rpc-max-request-size=1024M \
--bt-tracker="[$tracker_list]" --bt-max-peers=0 --bt-tracker-connect-timeout=300 --bt-stop-timeout=1200 --min-split-size=10M \
--follow-torrent=mem --split=10 \
--daemon=true --allow-overwrite=true --max-overall-download-limit=$MAX_DOWNLOAD_SPEED \
--max-overall-upload-limit=1K --max-concurrent-downloads=$MAX_CONCURRENT_DOWNLOADS \
--peer-id-prefix=-qB4350- --user-agent=qBittorrent/4.3.5 --peer-agent=qBittorrent/4.3.5 \
--disk-cache=64M --file-allocation=prealloc --continue=true \
--max-file-not-found=5 --max-tries=20 --auto-file-renaming=true \
--bt-enable-lpd=true --seed-time=0.01 --seed-ratio=1.0 \
--file-allocation=prealloc --max-file-not-found=5 --max-tries=5 --retry-wait=5 \
--auto-file-renaming=true --reuse-uri=true --http-accept-gzip=true --listen-port=49152-65535 \
--content-disposition-default-utf8=true --bt-tracker-connect-timeout=600 \
--dht-listen-port=51513 --enable-dht=true --enable-dht6=true \
--dht-file-path=/usr/src/app/dht.dat --dht-file-path6=/usr/src/app/dht6.dat \
--dht-entry-point=dht.transmissionbt.com:6881 \
--dht-entry-point6=dht.transmissionbt.com:6881 --netrc-path=/usr/src/app/.netrc
