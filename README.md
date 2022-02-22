# Idle Crypto Miner for Linux
  I noticed a lack of solutions to idle mining in Linux and decided to fix that. <s>Currently the entire project is just a simple python script that runs xmr-stak while idle, but I plan on making a gui (no promises though).I might also implement a configuration file so you're not only limited to running xmr-stak (again, no promises). If any of these plans come to fruition, it'll be during the summer when I have more time to code. </s> <br>
 See the roadmap section below to check on the applications development 
<h1> Dependencies </h1>
  -Python 3 <br>
  -Psutil <br>
  -Xprintidle <br>
  <br>
  On ubuntu these can be installed via the commands below,<br>


```
sudo apt-get install xprintidle
sudo apt-get install python3
sudo apt-get install python3-tk
sudo apt-get install pip
pip install psutil
```
### Roadmap
- [x] Make a script to run programs while idle
- [x] Add a simple GUI
- [ ] Expand the GUI to be more than one button (<s>stop button, </s>text entry to change amount of time until xmr starts)
- [ ] Find a way to config xmr-stak through the GUI
- [ ] Add the ability to change the mining program being used 
