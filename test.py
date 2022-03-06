from pytermii.termii import Termii

termii = Termii('TLjJb6ZnO66c4H3PmRlS9sb52Sygu68WgeOxXZeMpHfWoUO8AQQAOyEs9Rf7oH')

# print(termii.sender_id.fetch()['data'][0]['status'])
# termii.sender_id.request_id('MOBIELEPAY', 'your otp is 4757555,please do not disclose to anyone', 'MOBIELE')
# termii.message.send_message('2349133370715', 'MOBIELE', 'HI BOY', 'plain', 'generic')
# termii.message.send_message('2349133370715', 'MOBIELE', 'HI BOY', 'plain', 'generic','hhhj','gugug')
# termii.message.send_bulk_message(['2349133370715'], 'MOBIELE', 'HI BOY', 'plain', 'generic')
# termii.number.send_message('2349133370715', 'hi there')
# termii.template.send_template('2349133370715', 'hi there', 'hi there', 'hi there', 'hi there','sbs')
# termii.phonebook.create('test3','test3')
# e5993c4d-901b-4930-be75-08f45c9bf125
# result = termii.phonebook.fetch()
# print(termii.phonebook.update_by_name('old phonebook name', 'new phonebook name', "Phonebook for test"))
# termii.phonebook.update_by_id('e5993c4d-901b-4930-be75-08f45c9bf125', 'shddsh')
# termii.phonebook.delete_by_name('bkkkkkkkkkkkkkv')
# list_o = result['data']
# for i in list_o:
#     print(i['id'])

# termii.campaign.send_campaign_by_name('hellow', '234', 'MOBIELE', 'hi', 'generic', 'Plain', 'personalized',
#                                       'scheduled', '30-06-2022 6:00')

# termii.campaign.send_campaign_by_id('hellow', '234', 'MOBIELE', 'hi', 'generic', 'Plain', 'personalized',
#                                     'scheduled', '30-06-2022 6:00')
# termii.campaign.fetch_campaigns()
# C622469de269ab
# termii.campaign.fetch_campaign_history('C622469de269ab')
# termii.token.send_token('NUMERIC', '2349133370715', 'mobiele', 'dnd', 10, 5, 6, "< 1234 >", "Your pin is < 1234 >",
#                         "NUMERIC")
# termii.token.voice_token('2349133370715', 7, 7, 7)
# termii.token.voice_call('2349133370715', 23444)
# termii.token.in_app_token('NUMERIC', '2349133370715', 7, 7, 7)
# termii.token.verify_token('5c339a43-2d0b-4fcd-b384-e84b9fcab628', '9074955')
# termii.insight.balance()
# termii.insight.search('2347089357002')
# termii.insight.status('2347089357002', 'NG')
# termii.insight.history()
