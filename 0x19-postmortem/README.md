# Postmortem Review
![meme](https://github.com/Jolinejo/alx-system_engineering-devops/blob/master/0x19-postmortem/404_not_found.png)
## Summary

- **Duration of Outage:** Oct 31, 2023, 5 AM to Oct 31, 2023, 6 AM (GMT +2)
- **Issue Description:** Main server redirection malfunctioned, leading to users receiving a 404 not found error.
- **Root Cause:** Syntax error in the nginx config file, specifically affecting the lines responsible for redirection.
- **Resolution:** Nginx reinstalled, config file manually rewritten with extra attention to syntax, and automated file updated accordingly.

## Timeline

- **Oct 31, 2023, 5 AM (GMT +2):** Outage detected.
- **Oct 31, 2023, 5:05 AM (GMT +2):** Maintenance check reveals the issue.
- **Oct 31, 2023, 5:09 AM (GMT +2):** Verified existence of page files, checked config files.
- **Oct 31, 2023, 5:09 AM to 5:30 AM (GMT +2):** Investigated redirection code but found no errors.
- **Oct 31, 2023, 5:35 AM (GMT +2):** Nginx server reinstalled, new config file manually written, emphasizing the correction of the previous issue.

## Root Cause and Resolution

- **Root Cause:** Syntax error in the config file, introduced during an update using the sed command, affecting redirection lines.
- **Resolution Steps:**
  - Nginx reinstalled.
  - Config file manually rewritten, starting with the redirection.
  - 404 page added manually before using sed automation, ensuring thorough testing.
  - Sed command usage scrutinized for correctness.

## Corrective and Preventative Measures

- **Manual Checking/Testing:** Before deploying changes, conduct a manual examination for a visual check.
- **Config File Versioning:** Always keep an old version of config files before updates for easy reversion in case of errors.
- **Server Monitoring:** Implement monitoring to alert for issues that may not be easily noticeable.

