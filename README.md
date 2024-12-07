# SOARting_List

This is my gift to the Splunk SOAR community to help with sorting containers ingested into Splunk SOAR.

This is especially useful with the limitation of only being able to define 1 label in an On-Poll configuration for any given app in SOAR, but it can be used creatively with any method of container ingestion! This custom function allows you to make a quick playbook to change the label of the ingested container(s) to the desired destination label. Upon a label change, SOAR will run your desired playbooks set active on the new label.

Listed are both the .json and the .py files. If you want to upload it to your SOAR directly, you can download the .tgz file and upload it in your Custom Function menu!

- Hurricane Labs Blog Post: https://hurricanelabs.com/blog/splunk-soar-container-sorting-custom-function/
- In-Depth Tutorial: https://www.youtube.com/watch?v=d6oVcK2XWBY&ab_channel=HurricaneLabs


# SOAR 6.3.0 Known Issue:

**Edit:** I spoke with Splunk Support about this issue and they confirmed this is a bug with SOAR 6.3.0 when playbooks run after a label change, and has been fixed in SOAR 6.3.1. 
I was given their internal engineering Jira case number PSAAS-19708 which mentions: "playbooks are executing before the playbook row in the database has been created, causing the eventual playbook record to remain in the pending state."

---

I discovered a few issues with this custom function running in SOAR version 6.3.0. My current guess is this is due to the change/new feature regarding python runner scaling (or a bug generated from that change). Here are some work arounds you can use to still have the SOARting_List do it's thing - part of the time* (I am also opening up a bug report case with Splunk).

1. Problem: If you are ingesting a large volume of containers through the On-Poll action of a SOAR app, the secondary playbook(s) will not run and enter a perpetual "pending" state (this can be seen in `Administration > System Health > Playbook Run History` and clicking `pending` in the `status` tab). 

-   Solution/Workaround: I have solved this by making the min amount of runners 1, and the max amount of runners less than the amount of CPU cores my SOAR host has provisioned (typically 4-6). You can make this configuration change in  `Administration > Administration Settings > Playbook Execution`. This will run less playbooks at the same time, however playbooks ingested via On-Poll will not get stuck in a "pending" state at high volume.



2. Problem: Playbooks run on containers created via "Export Container" action from another SOAR instance, will **ALL** enter a perpetual "pending" state after being sorted and not run any additional playbooks automatically (this can also be seen in `Administration > System Health > Playbook Run History` and clicking `pending` in the `status` tab).

-   Solution/Workaround: If possible, use the SOARting_List on the source SOAR and set the label in the "Export Container" action as the output of the SOARting_List so that it arrives in your destination SOAR already sorted. I have not yet found a way to deal with this on the destination SOAR instance itself. 
