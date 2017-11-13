#coding: utf-8
import sys
import fastkvd
import glob
import datetime
import os





schema = {
    "afver" : "string",
    "devid" : "string",
    "ts" : "string",
    "szone" : "string",
    "dzone" : "string",
    "sip0" : "string",
    "sip1" : "string",
    "sip2" : "string",
    "dip0" : "string",
    "dip1" : "string",
    "dip2" : "string",
    "sport" : "string",
    "dport" : "string",
    "method" : "string",
    "host" : "string",
    "uri" : "string",
    "referer" : "string",
    "user_agent" : "string",
    "req_content_type" : "string",
    "req_body_len" : "string",
    "status_code" : "string",
    "rsp_content_type" : "string",
    "rsp_body_len" : "string",
    "duration" : "string",
    "req_head" : "string",
    "rsp_head" : "string",
    "req_body" : "string",
    "rsp_body" : "string"
}




outpath = "174021_6335.kvd"
record ={'dip1': '0', 'dip0': '3395925613', 'dip3': '0', 'dip2': '0', 'szone': '2', 'duration': '137', 'dzone': '2', 'sport': '32719', 'rsp_body_len': '95', 'ts': '1503417732934', 'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SCH-N719 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.5.489 U3/0.8.0 Mobile Safari/533.1', 'rsp_content_type': 'image/gif', 'req_content_type': '', 'status_code': '200', 'type': '1', 'method': 'GET', 'req_body': '', 'req_head': 'GET /bbx/images/gbhang/bg_1.gif HTTP/1.1\r\nHost: www.sgautism.com\r\nAccept: image/png,image/*;q=0.8,*/*;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nReferer: http://www.sgautism.com/\r\nUser-Agent: Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SCH-N719 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.5.489 U3/0.8.0 Mobile Safari/533.1\r\nclientip: 10.13.131.141\r\nx-real-ip: 140.205.109.191\r\nCookie: safedog-flow-item=60386B644FBB284954ECB59457C77840\r\nCache-Control: max-age=259200\r\nConnection: keep-alive\r\n\r\n', 'req_body_len': '0', 'host': 'www.sgautism.com', 'referer': 'http://www.sgautism.com/', 'sip1': '0', 'sip2': '0', 'sip3': '0', 'afver': 'TS2.5.15 Build20170613 ', 'rsp_head': 'HTTP/1.1 200 OK\r\nDate: Tue, 22 Aug 2017 15:58:53 GMT\r\nContent-Length: 95\r\nContent-Type: image/gif\r\nContent-Location: http://www.sgautism.com/bbx/images/gbhang/bg_1.gif\r\nLast-Modified: Mon, 14 Aug 2017 09:41:18 GMT\r\nAccept-Ranges: bytes\r\nETag: "5a558d7ae114d31:19bb96"\r\nServer: IIS\r\nX-Powered-By: WAF/2.0\r\n\r\n', 'uri': '/bbx/images/gbhang/bg_1.gif', 'rsp_body': 'GIF89a\x01\x00\x13\x00\xb3\x00\x00\xe7(9\xefak\xefQZ\xe70B\xefYc\xe7\x18!\xefAJ\xe7AR\xe7\x10!\xe7 1\xe7\x08\x18\xe7\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04', 'dport': '80', 'sip0': '2073474840'}
record_list = []
for i in range(1):
    record_list.append(record)
success = fastkvd.kvdwrite(record_list,outpath)
