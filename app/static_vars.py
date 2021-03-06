JobType = {
  'B' : '<div class="ui green label">Backup Job</div>',
  'M' : '<div class="ui violet label">Migrated Job</div>',
  'V' : '<div class="ui yellow label">Verify Job</div>',
  'R' : '<div class="ui blue label">Restore Job</div>',
  'C' : '<div class="ui yellow label">Console program (not in database)</div>',
  'I' : '<div class="ui green label">Internal or system Job</div>',
  'D' : '<div class="ui red label">Admin Job</div>',
  'A' : '<div class="ui yellow label">Archive Job (not implemented)</div>',
  'C' : '<div class="ui yellow label">Copy Job</div>',
  'M' : '<div class="ui yellow label">Migration Job</div>',
}

JobStatus = {
  'C' : '<div class="ui brown label">Created but not yet running</div>',
  'R' : '<div class="ui teal label">Running</div>',
  'B' : '<div class="ui pink label">Blocked</div>',
  'T' : '<div class="ui green label">Terminated normally</div>',
  'W' : '<div class="ui olive label">Terminated normally with warnings</div>',
  'E' : '<div class="ui orange label">Terminated in Error</div>',
  'e' : '<div class="ui yellow label">Non-fatal error</div>',
  'f' : '<div class="ui red label">Fatal error</div>',
  'D' : '<div class="ui purple label">Verify Differences</div>',
  'A' : '<div class="ui grey label">Canceled by the user</div>',
  'I' : '<div class="ui grey label">Incomplete Job</div>',
  'F' : '<div class="ui blue label">Waiting on the File daemon</div>',
  'S' : '<div class="ui blue label">Waiting on the Storage daemon</div>',
  'm' : '<div class="ui blue label">Waiting for a new Volume to be mounted</div>',
  'M' : '<div class="ui blue label">Waiting for a Mount</div>',
  's' : '<div class="ui blue label">Waiting for Storage resource</div>',
  'j' : '<div class="ui blue label">Waiting for Job resource</div>',
  'c' : '<div class="ui blue label">Waiting for Client resource</div>',
  'd' : '<div class="ui blue label">Wating for Maximum jobs</div>',
  't' : '<div class="ui blue label">Waiting for Start Time</div>',
  'p' : '<div class="ui blue label">Waiting for higher priority job to finish</div>',
  'i' : '<div class="ui grey label">Doing batch insert file records</div>',
  'a' : '<div class="ui yellow label">SD despooling attributes</div>',
  'l' : '<div class="ui yellow label">Doing data despooling</div>',
  'L' : '<div class="ui yellow label">Committing data (last despool)</div>',
}

JobLevel= { 
  'F' : '<div class="ui blue label">Full</div>', 
  'I' : '<div class="ui green label">Incremental</div>',# since last backup 
  'D' : '<div class="ui olive label">Differential</div>',# since last full backup 
  'S' : '<div class="ui yellow label">Since</div>',
  'C' : '<div class="ui purple label">Verify from catalog</div>',
  'V' : '<div class="ui purple  label">Verify safe from DB</div>',
  'O' : '<div class="ui purple  label">Verify Volume to catalog</div>', 
  'd' : '<div class="ui purple  label">Verify Disk to catalog</div>', 
  'A' : '<div class="ui purple  label">Verify data on volume</div>',
  'B' : '<div class="ui brown label">Base level job</div>', 
  ' ' : '<div class="ui black label">Restore/Admin</div>',
  'f' : '<div class="ui teal label">Virtual full</div>', 
}

VOLUME_STATUS_SEVERITY = {
  "Append": '<div class="ui yellow label">Append</div>',
  "Archive": '<div class="ui purple label">Archive</div>',
  "Disabled": '<div class="ui black label">Disabled</div>',
  "Full": '<div class="ui blue label">Full</div>',
  "Used": '<div class="ui blue label">Used</div>',
  "Cleaning": '<div class="ui purple  label">Cleaning</div>',
  "Purged": '<div class="ui green label">Purged</div>',
  "Recycle": '<div class="ui green label">Recycle</div>',
  "Read-Only": '<div class="ui red label">Read-Only</div>',
  "Error": '<div class="ui red label">Error</div>',
}


