#!/usr/bin/env python3
# coding=UTF-8
import sys

import paste
from bottle import run, route, request

@route('/json', method='POST')
def do_json():
    data = request.json
    message = data.get('message')
    resp = {}
    resp['rtn'] = 0
    resp['msg'] = 'Your message is %s.' % message
    resp['info'] = {
        "idCard":"322535199502035652",
        "name" : "aaron"
    }
    return  resp
@route('/test', method='Post')
def rsp_json():
    data = {
            "results": [
                {
                    "code": 0,
                    "error": "",
                    "status": "OK"
                }
            ],
            "items": [
                {
                    "id": "5d38cdf691ec48408c5695732d6f904a0000000005114641",
                    "seq_id": "85018177",
                    "feature": {
                        "type": "face",
                        "version": 24602,
                        "blob": "U09GMRpgAAAQAgAAAAEAAAAAAAAFAAAAAAAAAAAAAAD5XvgCGr5apgY5rgAaOWKj55QdwSAXIPRSPG3TNV7fO5iOQYsPqI1SjQFtOLceaM/1d62I9KKePXLpjCziVlaqHoiCnrxbeSrRn3BEmb/B4/126wnMRrEcFrqQDf4lYRLeGY35uJkXIOrNtCEp9wfM5a4kWk/EQaHN+sGM+Uj52prNgybvjsksbAV5txb+kgFcQfkx/gayAe0C1Ux3AdTg5SEPExdTV6UJ2GNnz83VHDbaAHyxVtx7iZgN7cxVP4NqHpDpybZ5TtKAcRGllo9zviagIWCWvBnVfm00L5Qwf9H1eJMlGMzxOrpTd/7rseGPU6rnUezNUP32iVhesfrW+xWl5zt8S2J5eFU7G3t5ZFfPqQTkZHzQtf1pYZLMWqK+w1IUEcb5l2hRKaNlAPLVqZsDckiyFo19+PiuN+M4M7Cq4P6jwgGJCGkYOxjQEi7tf2A7EWoH4jyvHlJZrNvjKaMqgY20OhgADlW4i4AKivTCEno6IFBJ2fs1EfdM4kAuD6L2WGF8Z8TJiHpE6b36HEMS7xsj5ET3gzFqTNTMEAF+o4AyxOHb0MrY+XOZEZ/ICKR7qtCuhatH80Ic7Qp5MYehCSxne2Llm0JtIhDsc4CB/aaKoPdVg5MwzuTgb4dUsRXFnNNtIEQ5YvY2b8lh7gNRXpKfDPr2CC/bJVw2rP6aNIrixT1RSWWKSN1sIJs="
                    },
                    "image_id": "sfd_5d38cdf691ec48408c5695732d6f9000/20190723-d06b3e40-0a580ae0009e-3d465e60-00004ea8",
                    "extra_info": "9oMwMWQBNpOXnoqoLNoX",
                    "meta_data": "eyJ0eXBlIjoxLCJmYWNlIjp7InF1YWxpdHkiOjAuODQ3ODU0MTQsInJlY3RhbmdsZSI6eyJ2ZXJ0aWNlcyI6W3sieCI6NzAsInkiOjE1Mn0seyJ4IjoyNzksInkiOjM1MH1dfSwiYW5nbGUiOnsieWF3IjotMi4yMDQxNDg4LCJwaXRjaCI6OC4wOTI3OTcsInJvbGwiOjMuNDM1Nzc2NX0sImxhbmRtYXJrcyI6W3sieCI6NzMsInkiOjE5NX0seyJ4Ijo3NCwieSI6MjA4fSx7IngiOjc2LCJ5IjoyMjF9LHsieCI6NzgsInkiOjIzNX0seyJ4Ijo4MSwieSI6MjQ4fSx7IngiOjg0LCJ5IjoyNjF9LHsieCI6ODgsInkiOjI3NH0seyJ4Ijo5MywieSI6Mjg3fSx7IngiOjk5LCJ5IjoyOTl9LHsieCI6MTA2LCJ5IjozMTF9LHsieCI6MTE1LCJ5IjozMjF9LHsieCI6MTI2LCJ5IjozMzB9LHsieCI6MTM3LCJ5IjozMzh9LHsieCI6MTUwLCJ5IjozNDV9LHsieCI6MTYzLCJ5IjozNTF9LHsieCI6MTc3LCJ5IjozNTN9LHsieCI6MTkxLCJ5IjozNTN9LHsieCI6MjA0LCJ5IjozNTF9LHsieCI6MjE3LCJ5IjozNDZ9LHsieCI6MjI4LCJ5IjozMzl9LHsieCI6MjM4LCJ5IjozMzB9LHsieCI6MjQ4LCJ5IjozMjF9LHsieCI6MjU2LCJ5IjozMTB9LHsieCI6MjYzLCJ5IjoyOTl9LHsieCI6MjY5LCJ5IjoyODd9LHsieCI6MjczLCJ5IjoyNzR9LHsieCI6Mjc1LCJ5IjoyNjF9LHsieCI6Mjc3LCJ5IjoyNDh9LHsieCI6Mjc5LCJ5IjoyMzV9LHsieCI6MjgwLCJ5IjoyMjJ9LHsieCI6MjgwLCJ5IjoyMDl9LHsieCI6MjgwLCJ5IjoxOTV9LHsieCI6Mjc5LCJ5IjoxODJ9LHsieCI6OTQsInkiOjE3N30seyJ4IjoxMDYsInkiOjE2NH0seyJ4IjoxMjIsInkiOjE2MX0seyJ4IjoxMzgsInkiOjE2MX0seyJ4IjoxNTQsInkiOjE2NX0seyJ4IjoxOTksInkiOjE2Mn0seyJ4IjoyMTQsInkiOjE1N30seyJ4IjoyMzAsInkiOjE1NH0seyJ4IjoyNDYsInkiOjE1Nn0seyJ4IjoyNjAsInkiOjE2N30seyJ4IjoxNzgsInkiOjE5Mn0seyJ4IjoxODAsInkiOjIwOH0seyJ4IjoxODEsInkiOjIyNX0seyJ4IjoxODMsInkiOjI0Mn0seyJ4IjoxNjEsInkiOjI1OX0seyJ4IjoxNzMsInkiOjI2MH0seyJ4IjoxODQsInkiOjI2MX0seyJ4IjoxOTUsInkiOjI1OH0seyJ4IjoyMDYsInkiOjI1Nn0seyJ4IjoxMTMsInkiOjE5N30seyJ4IjoxMjMsInkiOjE5MH0seyJ4IjoxNDUsInkiOjE5MH0seyJ4IjoxNTIsInkiOjE5OH0seyJ4IjoxNDMsInkiOjIwMH0seyJ4IjoxMjMsInkiOjIwMX0seyJ4IjoyMDQsInkiOjE5NX0seyJ4IjoyMTEsInkiOjE4Nn0seyJ4IjoyMzIsInkiOjE4M30seyJ4IjoyNDMsInkiOjE4OX0seyJ4IjoyMzQsInkiOjE5NH0seyJ4IjoyMTQsInkiOjE5Nn0seyJ4IjoxMDcsInkiOjE3NH0seyJ4IjoxMjIsInkiOjE3MX0seyJ4IjoxMzgsInkiOjE3MX0seyJ4IjoxNTQsInkiOjE3M30seyJ4IjoyMDAsInkiOjE3MH0seyJ4IjoyMTUsInkiOjE2N30seyJ4IjoyMzEsInkiOjE2NX0seyJ4IjoyNDYsInkiOjE2NX0seyJ4IjoxMzQsInkiOjE4OH0seyJ4IjoxMzMsInkiOjIwMn0seyJ4IjoxMzMsInkiOjE5Nn0seyJ4IjoyMjEsInkiOjE4Mn0seyJ4IjoyMjQsInkiOjE5Nn0seyJ4IjoyMjMsInkiOjE5MH0seyJ4IjoxNjUsInkiOjE5NX0seyJ4IjoxOTEsInkiOjE5M30seyJ4IjoxNjAsInkiOjIzN30seyJ4IjoyMDMsInkiOjIzNH0seyJ4IjoxNTQsInkiOjI1MX0seyJ4IjoyMTIsInkiOjI0N30seyJ4IjoxNTEsInkiOjI5Nn0seyJ4IjoxNjQsInkiOjI4OX0seyJ4IjoxNzgsInkiOjI4NX0seyJ4IjoxODYsInkiOjI4NX0seyJ4IjoxOTUsInkiOjI4M30seyJ4IjoyMDgsInkiOjI4NX0seyJ4IjoyMjEsInkiOjI5MH0seyJ4IjoyMTIsInkiOjI5OH0seyJ4IjoyMDAsInkiOjMwM30seyJ4IjoxODgsInkiOjMwNn0seyJ4IjoxNzUsInkiOjMwNn0seyJ4IjoxNjIsInkiOjMwMn0seyJ4IjoxNTYsInkiOjI5Nn0seyJ4IjoxNzIsInkiOjI5M30seyJ4IjoxODcsInkiOjI5M30seyJ4IjoyMDEsInkiOjI5MX0seyJ4IjoyMTYsInkiOjI5MX0seyJ4IjoyMDIsInkiOjI5Mn0seyJ4IjoxODcsInkiOjI5NX0seyJ4IjoxNzIsInkiOjI5NX0seyJ4IjoxMzMsInkiOjE5Nn0seyJ4IjoyMjMsInkiOjE5MH1dLCJhdHRyaWJ1dGVzIjp7ImFnZV9sb3dlcl9saW1pdCI6IjQwLjAwMDAwMCIsImFnZV91cF9saW1pdCI6IjUwLjAwMDAwMCIsImNhcF9zdHlsZSI6ImhhdF9zdHlsZV90eXBlX25vbmUiLCJldGhpY19jb2RlIjoib3RoZXJzIiwiZ2VuZGVyX2NvZGUiOiJmZW1hbGUiLCJnbGFzc19zdHlsZSI6ImdsYXNzZXNfc3R5bGVfdHlwZV9ub25lIiwibXVzdGFjaGVfc3R5bGUiOiJtdXN0YWNoZV9zdHlsZV90eXBlX25vbmUiLCJyZXNwaXJhdG9yX2NvbG9yIjoiY29sb3JfdHlwZV9ub25lIiwic2tpbl9jb2xvciI6InllbGxvdyIsInN0X2FnZSI6InN0X29sZCIsInN0X2FnZV92YWx1ZSI6IjQ1LjAwMDAwMCIsInN0X2V4cHJlc3Npb24iOiJzdF9jYWxtIn0sImF0dHJpYnV0ZXNfd2l0aF9zY29yZSI6eyJhZ2VfbG93ZXJfbGltaXQiOnsiY2F0ZWdvcnkiOiJhZ2VfbG93ZXJfbGltaXQiLCJ2YWx1ZSI6NDB9LCJhZ2VfdXBfbGltaXQiOnsiY2F0ZWdvcnkiOiJhZ2VfdXBfbGltaXQiLCJ2YWx1ZSI6NTB9LCJjYXBfc3R5bGUiOnsidHlwZSI6MiwiY2F0ZWdvcnkiOiJIQVRfU1RZTEVfVFlQRV9OT05FIiwidmFsdWUiOjAuOTk4OTM0fSwiZXRoaWNfY29kZSI6eyJ0eXBlIjoyLCJjYXRlZ29yeSI6Ik9USEVSUyIsInZhbHVlIjowLjgwOTk1fSwiZ2VuZGVyX2NvZGUiOnsidHlwZSI6MiwiY2F0ZWdvcnkiOiJGRU1BTEUiLCJ2YWx1ZSI6MC45NDQwNjl9LCJnbGFzc19zdHlsZSI6eyJ0eXBlIjoyLCJjYXRlZ29yeSI6IkdMQVNTRVNfU1RZTEVfVFlQRV9OT05FIiwidmFsdWUiOjAuOTk5OTgyfSwibXVzdGFjaGVfc3R5bGUiOnsidHlwZSI6MiwiY2F0ZWdvcnkiOiJNVVNUQUNIRV9TVFlMRV9UWVBFX05PTkUiLCJ2YWx1ZSI6MC45OTQ2MzR9LCJyZXNwaXJhdG9yX2NvbG9yIjp7InR5cGUiOjIsImNhdGVnb3J5IjoiQ09MT1JfVFlQRV9OT05FIiwidmFsdWUiOjAuOTkyNDI0fSwic2tpbl9jb2xvciI6eyJ0eXBlIjoyLCJjYXRlZ29yeSI6IllFTExPVyIsInZhbHVlIjowLjk5OTkyMn0sInN0X2FnZSI6eyJ0eXBlIjoyLCJjYXRlZ29yeSI6IlNUX09MRCIsInZhbHVlIjowLjY0Mjg1N30sInN0X2V4cHJlc3Npb24iOnsidHlwZSI6MiwiY2F0ZWdvcnkiOiJTVF9DQUxNIiwidmFsdWUiOjAuOTk3ODIxfX0sImZhY2Vfc2NvcmUiOjAuODk4MDI4N319",
                    "key": ""
                }
            ]
        }  
    return data

def main():
    # 阻塞的服务器，使用其他方式来实现非阻塞服务器
    # run(host='0.0.0.0', port=9001)

    # 通过paste 实现非阻塞的服务器  easy_install paste
    run(server='paste', host='0.0.0.0', port=9091)
if __name__ == "__main__":
    sys.exit(main())
