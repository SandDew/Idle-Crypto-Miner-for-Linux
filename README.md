# Idle Crypto Miner for Linux
  I noticed a lack of solutions to idle mining in Linux and decided to fix that. Currently the entire project is just a simple python script that runs xmr-stak while idle, but I plan on making a gui (no promises though). I might also implement a configuration file so you're not only limited to running xmr-stak (again, no promises). If any of these plans come to fruition, it'll be during the summer when I have more time to code.
<h1> Dependencies </h1>
  -Python 3 <br>
  -Psutil <br>
  -Xprintidle <br>
  <br>
  On ubuntu these can be installed via the commands below,<br>
  ```
  sudo apt-get install xprintidle <br>
  sudo apt-get install python3 <br>
  pip install psutil <br>
  ```
  
  
```
meson build
meson install -C build
```
  The ladder command might require you to install pip depending on your distribution
