import csv
from datetime import datetime

from github import Github


def write_commits(user_name, access_token, commit_count):
    g = Github(login_or_token=access_token)
    user = g.get_user(user_name)
    events = user.get_events()
    events_list = list()
    for event in events:
        event_data = list(event.raw_data.values())
        if event_data[1] == "PushEvent":
            # print(event_data[1], event_data[-1])
            events_list.append(datetime.strptime(event_data[-1], '%Y-%m-%dT%H:%M:%SZ'))
            if len(events_list) == int(commit_count):
                return events_list
    return events_list


def write_to_csv(file_name, commit_list):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for commit in commit_list:
            writer.writerow([commit])
    f.close()


def calc_mean_time(commit_list):
    print(commit_list)
    time_diff = list()
    for i in range(1, len(commit_list)):
        time_diff.append((commit_list[i-1] - commit_list[i]).seconds)
    return round(sum(time_diff) / len(time_diff), 2)


if __name__ == '__main__':
    user_name = input("please input your user name: ")
    print(f'your user name is {user_name}')
    access_token = input("please enter your personal access token: ")
    commit_count = input(f'enter last n commits to compute: ')
    print(f'commits to compute: {commit_count}')
    commits = write_commits(user_name=user_name, access_token=access_token,commit_count=commit_count)
    write_to_csv(file_name='commits.csv', commit_list=commits)
    print(f'mean time for the last {commit_count} is {calc_mean_time(commit_list=commits)}')






