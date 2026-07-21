Read the Apache-style access log at `/app/access.log` and write a traffic summary as
JSON to `/app/report.json`. Do not modify the input log.

1. `/app/report.json` must exist, parse as a JSON object, and contain exactly the
   keys `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` must be the integer count of all non-empty request lines, and
   `unique_ips` must be the integer count of distinct client IP addresses in the
   first field of those lines.
3. `top_path` must be the string request path that occurs most often in the quoted
   HTTP request field. If paths tie, use the one that appears first in the log.
