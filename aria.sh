export MAX_DOWNLOAD_SPEED=0
tracker_list=$(curl -Ns https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt | awk '$1' | tr '\n' ',')
export MAX_CONCURRENT_DOWNLOADS=5
aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port 6800 --check-certificate=false \
   --max-connection-per-server=14 --rpc-max-request-size=1024M \
   --bt-tracker="[$tracker_list]" --bt-max-peers=0 --seed-time=0.01 --min-split-size=10M \
   --follow-torrent=mem --split=10 \
   --daemon=true --allow-overwrite=true --max-overall-download-limit=$MAX_DOWNLOAD_SPEED \
   --max-overall-upload-limit=0 --max-concurrent-downloads=$MAX_CONCURRENT_DOWNLOADS \
   --bt-request-peer-speed-limit=0 --dht-listen-port=51513 \
   --enable-dht=true --enable-dht6=false --dht-file-path=/usr/src/app/dht.dat --dht-file-path6=/usr/src/app/dht6.dat \
   --dht-entry-point=dht.transmissionbt.com:6881 --dht-entry-point6=dht.transmissionbt.com:6881