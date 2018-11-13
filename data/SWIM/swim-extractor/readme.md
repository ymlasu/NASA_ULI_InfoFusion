# Generation

Schemas from 
https://www.fixm.aero/fixm_30.pl
https://www.fixm.aero/fixm_nas_extension_30.pl

Note: I had to patch a bug in pyxb to make it trace the schemas correctly.
The `utility.diff` file shows the changes, which should be applied to `utility.py`. 
On my system, the path is:
`C:\Users\awhittington\AppData\Local\Programs\Python\Python37\Lib\site-packages\pyxb\utils\utility.py`

Command run: 
`C:\Users\awhittington\Documents\SWIM> C:\Users\awhittington\AppData\Local\Programs\Python\Python37\python.exe C:\Users\awhittington\AppData\Local\Programs\Python\Python37\Scripts\pyxbgen -u schemas\SFDPSSchema-1.3.8.xsd -m fdps -u schemas\core\Fixm.xsd -m fixm -u schemas\extensions\nas\Nas.xsd -m nas`

# SMES
Commands run:
`C:\Users\awhittington\Documents\SWIM>C:\Users\awhittington\AppData\Local\Programs\Python\Python37\python.exe C:\Users\awhittington\AppData\Local\Programs\Python\Python37\Scripts\pyxbgen -u "R3.3 Schema\externalInterfaces\smes\SMESSurfaceMovementEventMessage.xsd" -m smes3 -u "R3.3 Schema\externalInterfaces\smes\sd\asdexmessage.xsd" -m asdex3 --module-prefix smes3`
`C:\Users\awhittington\Documents\SWIM>C:\Users\awhittington\AppData\Local\Programs\Python\Python37\python.exe C:\Users\awhittington\AppData\Local\Programs\Python\Python37\Scripts\pyxbgen -u "R4 Schema\externalInterfaces\smes\SMESSurfaceMovementEventMessage.xsd" -m smes4 -u "R4 Schema\externalInterfaces\smes\sd\asdexmessage.xsd" -m asdex4 --module-prefix smes4`

Making use of `--module-prefix` this time, because the two different versions share schema/typenames and they can't all coexist in one folder.