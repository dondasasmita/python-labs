data = [{'sharing_service': 'COPY_PASTE', 'num_of_shares': '59'}, {'sharing_service': 'TELEGRAM', 'num_of_shares': '12'}, {'sharing_service': 'OTHER', 'num_of_shares': '11'}, {'sharing_service': 'DIGG', 'num_of_shares': '10'}, {'sharing_service': 'KAKAO', 'num_of_shares': '4'}, {'sharing_service': 'WECHAT', 'num_of_shares': '4'}, {'sharing_service': 'SKYPE', 'num_of_shares': '3'}, {'sharing_service': 'WEIBO', 'num_of_shares': '3'}, {
    'sharing_service': 'FACEBOOK_MESSENGER', 'num_of_shares': '2'}, {'sharing_service': 'REDDIT', 'num_of_shares': '2'}, {'sharing_service': 'TEXT_MESSAGE', 'num_of_shares': '2'}, {'sharing_service': 'TUMBLR', 'num_of_shares': '2'}, {'sharing_service': 'FACEBOOK', 'num_of_shares': '1'}, {'sharing_service': 'TWITTER', 'num_of_shares': '1'}, {'sharing_service': 'VKONTAKTE', 'num_of_shares': '1'}, {'sharing_service': 'WHATS_APP', 'num_of_shares': '1'}]

counter = 0
total = 0
new_array = []
for i in data:
    if counter < 5:
        new_array.append(i)
    else:
        total += int(i["num_of_shares"])
    counter += 1
    if counter == len(data):
        new_array.append({'sharing_service': 'Others', 'num_of_shares': total})


print(new_array)
print(total)
