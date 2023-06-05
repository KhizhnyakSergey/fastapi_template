import uuid
# from functools import singledispatch


# @singledispatch
# def x(x: str):
#     print(10)

# @x.register
# def _(x: int):
#     print(15)

# # x('5')
# import base64, hashlib, uuid

# from cryptography.fernet import Fernet
# # print(base64.b64encode(b'''MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCcB+HbHb/U+de2PJp8VYIo0g6a
# # mfzYwlulSBMWbJFE4+teh0PgLv+T3oRj5dkezFhBC9HIDzZbbh7w61aWEt/srbD5
# # yuSAnZACVKfw4+PVV0lbwDM3ITHWwcALbzB6dkwEO0I047K5KgbXhoq9siI1+wFu
# # NrBwUWInQGIi+Sk9gwIDAQAB'''))
# key = b'scukDc6wGttlZAuFDjrcsq0WUn-LBlr1fsmQam_fEGQ='
# # key = Fernet.generate_key()
# x = 'c420ad11-517f-461f-927f-59ee5dc36232'
# cipher = Fernet(key)
# # x = str(uuid.uuid4())

# first_encrypt = cipher.encrypt(x.encode())
# second_encrypt = base64.b64encode(first_encrypt)
# # print(second_encrypt.decode())
# first_decrypt = base64.b64decode(second_encrypt.decode())
# second_decrypt = cipher.decrypt(first_decrypt)
# # print(second_decrypt.decode())
# print(second_encrypt)
# import smtplib
# from email.mime.text import MIMEText

# sender = 'olegprog23@gmail.com' 
# pwd = 'tbdipjjnosuxlnub'
# reciever = 'dimaprog22@gmail.com'
# message = MIMEText('''<body><div id=":7p" class="ii gt" jslog="20277; u014N:xr6bB; 1:WyIjdGhyZWFkLWY6MTc2MDYyMjcxNDQzNDY4Njk1NiIsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsW11d; 4:WyIjbXNnLWY6MTc2MDYyMzMxMzk0NDkzMTM1NyIsbnVsbCxbXV0."><div id=":7o" class="a3s aiL msg-1994166543447853440 adM"><div class="HOEnZb"><div class="adm"><div id="q_34" class="ajR h4" data-tooltip="Скрыть развернутую часть" aria-label="Скрыть развернутую часть" aria-expanded="true"><div class="ajT"></div></div></div><div class="im"><u></u>


	
	
	
	

#     <div style="font-size:16px;background-color:#fdfdfd;margin:0;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;line-height:1.5;height:100%!important;width:100%!important">
#     <table bgcolor="#fdfdfd" style="box-sizing:border-box;border-spacing:0;width:100%;background-color:#fdfdfd;border-collapse:separate!important" width="100%">
#         <tbody>
#             <tr>
#                 <td style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top" valign="top">&nbsp;</td>
#                 <td style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top;display:block;width:600px;max-width:600px;margin:0 auto!important" valign="top" width="600">
#                 <div style="box-sizing:border-box;display:block;max-width:600px;margin:0 auto;padding:10px"><span style="color:transparent;display:none;height:0;max-height:0;max-width:0;opacity:0;overflow:hidden;width:0">Let's verify your single sender so you can start sending email.</span>
#                 <div style="box-sizing:border-box;width:100%;margin-bottom:30px;margin-top:15px">
#                 <table style="box-sizing:border-box;width:100%;border-spacing:0;border-collapse:separate!important" width="100%">
#                     <tbody>
#                         <tr>
#                             <td align="left" style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top;text-align:left" valign="top"><span><a href="https://u298828.ct.sendgrid.net/ss/c/aJrxWzXarbnB62JtyTgHZh5XEDz4JqqJLmJngDXkiXpVV0LyaA0ZO26ibGXtVxzE6LS57o8OZJs25HtQESh8nyWQuGVCrCyn4QJ_juXOWIQBvZZBTa_XRUqBIUF1gNOw/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h8/FGSx36AkqHhiVvlGDGlsDXc70ahG9cssS3YnONv-q6c" style="box-sizing:border-box;color:#348eda;font-weight:400;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/aJrxWzXarbnB62JtyTgHZh5XEDz4JqqJLmJngDXkiXpVV0LyaA0ZO26ibGXtVxzE6LS57o8OZJs25HtQESh8nyWQuGVCrCyn4QJ_juXOWIQBvZZBTa_XRUqBIUF1gNOw/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h8/FGSx36AkqHhiVvlGDGlsDXc70ahG9cssS3YnONv-q6c&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw0D84RdCc2J2wpJBc1Y9fgn"><img alt="SendGrid" height="30" src="https://ci5.googleusercontent.com/proxy/EcjfSmmeCY5IVY2tiuLUh7-cRGDg_BVGsXX53NYzuYJgJhjBvY8_BNJpKncfMYh4wnJLQpAI81Bsejwj5KKNRl5svc5h85K0ZnxlZefbilBSpv3vUxMtrA=s0-d-e1-ft#https://uiux.s3.amazonaws.com/style-guide/img/sg-twilio-lockup@2x.png" style="max-width:100%;border-style:none;width:137px;height:30px" width="137" class="CToWUd" data-bit="iit"></a></span></td>
#                         </tr>
#                     </tbody>
#                 </table>
#                 </div>
    
#                 <div style="box-sizing:border-box;width:100%;margin-bottom:30px;background:#ffffff;border:1px solid #f0f0f0">
#                 <table style="box-sizing:border-box;width:100%;border-spacing:0;border-collapse:separate!important" width="100%">
#                     <tbody>
#                         <tr>
#                             <td style="box-sizing:border-box;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top;padding:30px" valign="top">
#                             <table style="box-sizing:border-box;width:100%;border-spacing:0;border-collapse:separate!important" width="100%">
#                                 <tbody>
#                                     <tr>
#                                         <td style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top" valign="top">
#                                         <h2 style="margin:0;margin-bottom:30px;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-weight:300;line-height:1.5;font-size:24px;color:#294661!important">Let's verify your single sender so you can start sending email.</h2>
    
#                                         <p style="margin:0;margin-bottom:30px;color:#294661;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;font-weight:300"><strong><a href="mailto:olegprog23@gmail.com" target="_blank">olegprog23@gmail.com</a></strong></p>
    
#                                         <p style="margin:0;margin-bottom:30px;color:#294661;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;font-weight:300"><small>Your link is active for 48 hours. After that, you will need to resend the verification email.</small></p>
#                                         </td>
#                                     </tr>
#                                     <tr>
#                                         <td style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top" valign="top">
#                                         <table cellpadding="0" cellspacing="0" style="box-sizing:border-box;border-spacing:0;width:100%;border-collapse:separate!important" width="100%">
#                                             <tbody>
#                                                 <tr>
#                                                     <td align="center" style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top;padding-bottom:15px" valign="top">
#                                                     <table cellpadding="0" cellspacing="0" style="box-sizing:border-box;border-spacing:0;width:auto;border-collapse:separate!important">
#                                                         <tbody>
#                                                             <tr>
#                                                                 <td align="center" bgcolor="#348eda" style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top;background-color:#348eda;border-radius:2px;text-align:center" valign="top"><a href="https://u298828.ct.sendgrid.net/ss/c/KeecV0-eUYdPWIcLaNcQIk8KHRb5oSkirDE8JL2zHb43giRdffV4A9P-M2zuA5z8yn9k718SwxXLtsouqB_R0O55ERXeLn0ds7a6ThnkVIhw5R4CdUnuKmbjjJGs4N_u-Y_q1d42X8m2X86YFqjRxy-yFwyfSuD-yD6Wfgn_L7WasAyL1HVctcBOvFZeYsbLeKHAC99P4w_snJ9q7EH2tn0Dx1wADUksvBFSJwltHlMvng_oKJUKphEbYJuVwX_AEtwiq5-9M5xbuacOrkz8nb9TN155mYToC8-j1a8OHtcqFeZNNpE21KGDB03pdO1T4o6jTwsVEdy6QNnHaFBQKtCOTZM_QVB_IDyQgbMGLw1QLnt8znsic9Kpeu6FN_tu-PiUrQxLN77bfWT335EnVzFyz__nNoEROYi3dnQfdpHPJrGZtkL1ooN0Wm9_bqj7JoKXLkjTWRxPHDqVIVo3-_jMq-qcemoOJokv77oSPAU/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h9/0Rs4c2FEO2u2vwktx0UDEDsCdjyDZ5uoLM8SHDu1Lb0" style="box-sizing:border-box;border-color:#348eda;font-weight:400;text-decoration:none;display:inline-block;margin:0;color:#ffffff;background-color:#348eda;border:solid 1px #348eda;border-radius:2px;font-size:14px;padding:12px 45px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/KeecV0-eUYdPWIcLaNcQIk8KHRb5oSkirDE8JL2zHb43giRdffV4A9P-M2zuA5z8yn9k718SwxXLtsouqB_R0O55ERXeLn0ds7a6ThnkVIhw5R4CdUnuKmbjjJGs4N_u-Y_q1d42X8m2X86YFqjRxy-yFwyfSuD-yD6Wfgn_L7WasAyL1HVctcBOvFZeYsbLeKHAC99P4w_snJ9q7EH2tn0Dx1wADUksvBFSJwltHlMvng_oKJUKphEbYJuVwX_AEtwiq5-9M5xbuacOrkz8nb9TN155mYToC8-j1a8OHtcqFeZNNpE21KGDB03pdO1T4o6jTwsVEdy6QNnHaFBQKtCOTZM_QVB_IDyQgbMGLw1QLnt8znsic9Kpeu6FN_tu-PiUrQxLN77bfWT335EnVzFyz__nNoEROYi3dnQfdpHPJrGZtkL1ooN0Wm9_bqj7JoKXLkjTWRxPHDqVIVo3-_jMq-qcemoOJokv77oSPAU/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h9/0Rs4c2FEO2u2vwktx0UDEDsCdjyDZ5uoLM8SHDu1Lb0&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw3QxGpZDbyJRLWOXZb32Ugv">Verify Single Sender</a></td>
#                                                             </tr>
#                                                         </tbody>
#                                                     </table>
#                                                     </td>
#                                                 </tr>
#                                             </tbody>
#                                         </table>
#                                         </td>
#                                     </tr>
#                                 </tbody>
#                             </table>
#                             </td>
#                         </tr>
#                     </tbody>
#                 </table>
#                 </div>
    
#                 <div style="box-sizing:border-box;clear:both;width:100%">
#                 <table style="box-sizing:border-box;width:100%;border-spacing:0;font-size:12px;border-collapse:separate!important" width="100%">
#                     <tbody>
#                         <tr style="font-size:12px">
#                             <td align="center" style="box-sizing:border-box;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;vertical-align:top;font-size:12px;text-align:center;padding:20px 0" valign="top"><span style="float:none;display:block;text-align:center"><a href="https://u298828.ct.sendgrid.net/ss/c/aJrxWzXarbnB62JtyTgHZh5XEDz4JqqJLmJngDXkiXpVV0LyaA0ZO26ibGXtVxzE6LS57o8OZJs25HtQESh8nyWQuGVCrCyn4QJ_juXOWIQBvZZBTa_XRUqBIUF1gNOw/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h10/txyDYaXFJD4Qwep79N--SmtlGBGlbPmHQnJjiXZfR0E" style="box-sizing:border-box;color:#348eda;font-weight:400;text-decoration:none;font-size:12px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/aJrxWzXarbnB62JtyTgHZh5XEDz4JqqJLmJngDXkiXpVV0LyaA0ZO26ibGXtVxzE6LS57o8OZJs25HtQESh8nyWQuGVCrCyn4QJ_juXOWIQBvZZBTa_XRUqBIUF1gNOw/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h10/txyDYaXFJD4Qwep79N--SmtlGBGlbPmHQnJjiXZfR0E&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw3JtXQHt8zRRohi7Jglj8P5"><img alt="SendGrid" height="16" src="https://ci5.googleusercontent.com/proxy/EcjfSmmeCY5IVY2tiuLUh7-cRGDg_BVGsXX53NYzuYJgJhjBvY8_BNJpKncfMYh4wnJLQpAI81Bsejwj5KKNRl5svc5h85K0ZnxlZefbilBSpv3vUxMtrA=s0-d-e1-ft#https://uiux.s3.amazonaws.com/style-guide/img/sg-twilio-lockup@2x.png" style="max-width:100%;border-style:none;font-size:12px;width:91px;height:20px" width="91" class="CToWUd" data-bit="iit"></a></span>
    
#                             <p style="color:#294661;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:12px;font-weight:400;margin-bottom:5px;margin:10px 0 20px">Send with Confidence</p>
    
#                             <p style="margin:0;color:#294661;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-weight:300;font-size:12px;margin-bottom:5px">© SendGrid Inc. 1801 California Street, Suite 500, Denver, CO 80202 USA</p>
    
#                             <p style="margin:0;color:#294661;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-weight:300;font-size:12px;margin-bottom:5px"><a href="https://u298828.ct.sendgrid.net/ss/c/aJrxWzXarbnB62JtyTgHZod5YIKSHURpGzKJw7a09DNr-40E-Dd1BWWs4kAj-PFhnguHA_aBMtXbSR7UXmcNoWDvH8h6K_kxJBEI07WfQujr832w6s9x1WUnzDyg0IYz/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h11/Zq5uQAhiWdiwPcxbZUFA95qWqdWpbAWYwGaJXtoMcQo" style="box-sizing:border-box;color:#348eda;font-weight:400;text-decoration:none;font-size:12px;padding:0 5px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/aJrxWzXarbnB62JtyTgHZod5YIKSHURpGzKJw7a09DNr-40E-Dd1BWWs4kAj-PFhnguHA_aBMtXbSR7UXmcNoWDvH8h6K_kxJBEI07WfQujr832w6s9x1WUnzDyg0IYz/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h11/Zq5uQAhiWdiwPcxbZUFA95qWqdWpbAWYwGaJXtoMcQo&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw1xXYeDk_twTqY_QI71ozEJ">Blog</a> <a href="https://u298828.ct.sendgrid.net/ss/c/poE2veomcy6ylfr_Ro2nmJBxBtdj2jlD_pc-sebDocM8ko394IziGpDMpT4ZGZ-LEXGBGghf9N-ccSv89MC78imVixiLg8UAB6hsAS5MebJefIHn_46zAm7CkA9251kmZMmPuc7tl3LQ2PZKCucmIA/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h12/UjSIlp5Sgnn8r0Nx1qTxo29B-tjKtfwgAaZsMn4TzTU" style="box-sizing:border-box;color:#348eda;font-weight:400;text-decoration:none;font-size:12px;padding:0 5px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/poE2veomcy6ylfr_Ro2nmJBxBtdj2jlD_pc-sebDocM8ko394IziGpDMpT4ZGZ-LEXGBGghf9N-ccSv89MC78imVixiLg8UAB6hsAS5MebJefIHn_46zAm7CkA9251kmZMmPuc7tl3LQ2PZKCucmIA/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h12/UjSIlp5Sgnn8r0Nx1qTxo29B-tjKtfwgAaZsMn4TzTU&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw0a1KE7q1WB36f1XIXIjZC5">GitHub</a> <a href="https://u298828.ct.sendgrid.net/ss/c/nf0RiBa0cBb3Zw-MD73wzUaCuz7rjp_J-Qb6sEryuxCL1FBN0Gbg4m2vjlRzeDt8RFqlKvNWHeTtdLub9p5NZOFcxbahDxK0DJu4ya_qV8Ld0V2Ps9Tacg-1U2fSCC6wFaPPPU3VMjYe21jOMBC7Fg/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h13/wzs6vfPd_NoBo703XRnOWTosdg6yTPD2vXOzbrJdem0" style="box-sizing:border-box;color:#348eda;font-weight:400;text-decoration:none;font-size:12px;padding:0 5px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/nf0RiBa0cBb3Zw-MD73wzUaCuz7rjp_J-Qb6sEryuxCL1FBN0Gbg4m2vjlRzeDt8RFqlKvNWHeTtdLub9p5NZOFcxbahDxK0DJu4ya_qV8Ld0V2Ps9Tacg-1U2fSCC6wFaPPPU3VMjYe21jOMBC7Fg/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h13/wzs6vfPd_NoBo703XRnOWTosdg6yTPD2vXOzbrJdem0&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw38Fbi12qUcVSHJJcdScKUD">Twitter</a> <a href="https://u298828.ct.sendgrid.net/ss/c/6BjF4NuCrD95SSp8XzpujnUSEaMzg6VcI9g2QJaIXF0lzDZ3KL_StHgYF7m7f9QVxgv5rrrqjgicEnZIFOHUYUk7P-c_EgZNjzOrAm8u6vmJoBViBEME6KvbdS8DMijXlaLz_0NNKI9dNagsLdUVww/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h14/3sEgD_x7s93omLjoR8sXAnNIZdRrOqoI8ZsWOSgldEw" style="box-sizing:border-box;color:#348eda;font-weight:400;text-decoration:none;font-size:12px;padding:0 5px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/6BjF4NuCrD95SSp8XzpujnUSEaMzg6VcI9g2QJaIXF0lzDZ3KL_StHgYF7m7f9QVxgv5rrrqjgicEnZIFOHUYUk7P-c_EgZNjzOrAm8u6vmJoBViBEME6KvbdS8DMijXlaLz_0NNKI9dNagsLdUVww/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h14/3sEgD_x7s93omLjoR8sXAnNIZdRrOqoI8ZsWOSgldEw&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw1ejVG6FC8QUcdxE0467Tsu">Facebook</a> <a href="https://u298828.ct.sendgrid.net/ss/c/6BjF4NuCrD95SSp8XzpujmDxm1JH5OuoZX5dC1VxTYT8OdD42xFHUU_JV93Czl-LY24HF-3DVeUIP94wswG96ZieLv6A-d0yiNaF2chi7mSoddFIFGqdZ9ztmg-1CUBMEFmMUfE0krwm6R1DeDvyOg/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h15/DCHjcaE5o2odri7w5pM96hYe5L_VU-mpesTn01N9C0Q" style="box-sizing:border-box;color:#348eda;font-weight:400;text-decoration:none;font-size:12px;padding:0 5px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://u298828.ct.sendgrid.net/ss/c/6BjF4NuCrD95SSp8XzpujmDxm1JH5OuoZX5dC1VxTYT8OdD42xFHUU_JV93Czl-LY24HF-3DVeUIP94wswG96ZieLv6A-d0yiNaF2chi7mSoddFIFGqdZ9ztmg-1CUBMEFmMUfE0krwm6R1DeDvyOg/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/h15/DCHjcaE5o2odri7w5pM96hYe5L_VU-mpesTn01N9C0Q&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw2tSZOOhBp1rC7cCtZukAtI">LinkedIn</a></p>
#                             </td>
#                         </tr>
#                     </tbody>
#                 </table>
#                 </div>
#                 </div>
#                 </td>
#                 <td style="box-sizing:border-box;padding:0;font-family:'Open Sans','Helvetica Neue','Helvetica',Helvetica,Arial,sans-serif;font-size:16px;vertical-align:top" valign="top">&nbsp;</td>
#             </tr>
#         </tbody>
#     </table>
    
    
#     Email sent using <a href="http://sendgrid.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://sendgrid.com&amp;source=gmail&amp;ust=1679148025282000&amp;usg=AOvVaw3kugJuP2UC2V18xzvCnXWs">SendGrid.com</a>.<img src="https://ci3.googleusercontent.com/proxy/ALWTte3UviHA6k49V-Md4RypE0gDzldoGzaj0VCuzsk66ZuVDvG6cYcCECaoC0vH9aNGY-nqwtTm3jUQcqsvTPOpwaT74ubIk9VUf0nmMNVLNY-UfLTnho1IsbOIHS9_Q2ZIDK3-1Nprf1wnRWbBkQ=s0-d-e1-ft#https://u298828.ct.sendgrid.net/ss/o/PJguMbS879ys4Oj5UHAMSw/3uk/-cnBFnk1S9-Sx6V5m9dvlQ/ho.gif" alt="" width="1" height="1" border="0" style="height:1px!important;width:1px!important;border-width:0!important;margin-top:0!important;margin-bottom:0!important;margin-right:0!important;margin-left:0!important;padding-top:0!important;padding-bottom:0!important;padding-right:0!important;padding-left:0!important" class="CToWUd" data-bit="iit"></div>
    
#     -</div></div></div></div></body>''', 'html')
# message['Subject'] = 'Hui?'
# message['From'] = sender
# message['To'] = reciever
# with smtplib.SMTP('smtp.gmail.com', 587) as server:
#     server.starttls()
#     server.login(user=sender, password=pwd)
#     server.sendmail(sender, reciever, message.as_string())
#     # server.sendmail(sender, reciever, 'Privet ti che pes ebuchiy')


from services.auth.confirmation import send_email
import schemas

import asyncio

asyncio.run(send_email(
    'dimaprog22@gmail.com', 
    '123456', 
    schemas.UserWithID(
        name='alibaba',
        surname='alibabovich',
        login='alibab12',
        photo='nudes',
        id='chlen1',
        is_active=False
    )))