"""Fictional workshop HTTP fixtures, loopback only. No account data or credentials."""
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
from pathlib import Path
class Fixture(BaseHTTPRequestHandler):
 def log_message(self,*a):pass
 def do_GET(self):
  if self.path=='/training/parts':
   payload={'trainingOnly':True,'source':'local-workshop-fixture','parts':[{'partCode':'FUSE-T4','available':17},{'partCode':'FILTER-Q8','available':8},{'partCode':'DIAL-B2','available':0}],'inspectionNotice':'A human must review equipment safety. This is invented teaching data.'};body=json.dumps(payload).encode();self.send_response(200);self.send_header('Content-Type','application/json')
  elif self.path=='/training/controlled-error':
   body=json.dumps({'trainingOnly':True,'error':'Deliberate training failure','retryChangesNothing':True}).encode();self.send_response(503);self.send_header('Content-Type','application/json')
  elif self.path=='/training/workshop':
   body=b'<!doctype html><html lang="en"><meta charset="utf-8"><title>Fictional Workshop Training</title><h1>Workshop training fixture</h1><p class="notice">Invented data. No real bookings.</p><ul id="slots"><li>Morning bench: 09:30</li><li>Afternoon bench: 14:15</li></ul><table id="parts"><tr><th>Part</th><th>Stock</th></tr><tr><td>FUSE-T4</td><td>17</td></tr><tr><td>FILTER-Q8</td><td>8</td></tr><tr><td>DIAL-B2</td><td>0</td></tr></table></html>';self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8')
  else:
   body=b'{"trainingOnly":true,"error":"unknown fixture path"}';self.send_response(404);self.send_header('Content-Type','application/json')
  self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
if __name__=='__main__':HTTPServer(('127.0.0.1',5682),Fixture).serve_forever()
