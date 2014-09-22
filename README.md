Cheating Detection
==================

Authors: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Supervisor: Hussein Suleman
Date: 20 September 2014

Consists of two parts the matching background worker and the web ui.

Execution steps
---------------
1. Open two consoles
2. Install plyj by running 'setup.py install' in the plyj folder
In console 1 run the following
3. source ve/bin/activate
4. cd cheaters
5. python matchesworker.py
In console 2 run the following
6. source ve/bin/activate
7. cd server
8. python server.py
Open http://localhost:5000 in your web browser for the lecturer page.

A simulated student submission page is available at http://localhost:5000/student/submit
