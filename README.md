# SOARting_List

This is my gift to the Splunk SOAR community to help with sorting containers ingested into Splunk SOAR.

This is especially useful with the limitation of only being able to define 1 label in an On-Poll configuration for any given app in SOAR. This custom function allows you to make a quick playbook to change the label of the ingested container(s) to the desired destination label. Upon a label change, SOAR will run your desired playbooks set active on the new label.

Listed are both the .json and the .py files. If you want to upload it to your SOAR directly, you can download the .tgz file and upload it in your Custom Function menu!
