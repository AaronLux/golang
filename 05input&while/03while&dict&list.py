unconfirmed_users = ["aaron","dopa","john"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user + "...")
    print(current_user.title() + " Verified.")
    # 只有上面的调用返回成功才能加入，这里模拟的逻辑不严谨
    confirmed_users.append(current_user)

print("The following users have been verified:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())