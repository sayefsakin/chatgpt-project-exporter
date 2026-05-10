### Save the project
- open any chatgpt project folder in the browser
- right click and select inspect
- right click on the top most element and selct copy, and then outer HTML
- save to a html file (for example test.html)
- open the html file and check that all contents are there

### Extract CID
- open the python file `cid-extractor.py` and update the html file name in line 5
- pip instal bs4
- run the cid-extractory.py file. This will output the cid and title of each conversation as a javascript json list.
- copy all except the last comma.
- open the `chatgpt-project-exporter.js` and paste overwrite from line 222 for `conversations` variable.

### Running the javascript to export
- Go to chrome inspect again and select console.
- copy the entire `chatgpt-project-exporter.js` and paste in the console. Then hit enter.
- This will take some time and show status of how many conversations converted.
- This will produce a zip file. Save the zip file and extract.
- Now you will have this exported in html, json, and markdown format.


------

### Acknowledgements
This exporter is an extension and codes are forked from [chatgpt-chat-exporter](https://github.com/rashidazarang/chatgpt-chat-exporter). Original console exporter [code is here](https://gist.githubusercontent.com/ocombe/1d7604bd29a91ceb716304ef8b5aa4b5/raw/export-chatgpt-console.js).

Track ChatGPT backend api [here](https://github.com/terminalcommandnewsletter/everything-chatgpt).
