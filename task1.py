import subprocess
import csv


def get_ping_data(domain):
    ping = subprocess.Popen(["ping",'-n','1', domain],shell=True,stdout=subprocess.PIPE)
    decoded_ping = ping.stdout.read().decode('cp866')
    split_ping = decoded_ping.split(' ')

    ip = split_ping[4][1:-1]
    number_of_bytes = split_ping[6]
    time = split_ping[13][6:-2]
    ttl = split_ping[14][4:-14]
    packages_sent = split_ping[24][0]
    packages_received = split_ping[27][0]
    packages_lost = split_ping[30][0]
    percent_lost_pack = split_ping[34][1:]
    min_time = split_ping[45][:-5]
    max_time = split_ping[48]
    avg_time = split_ping[52]
    
    result_row = [domain, ip, number_of_bytes, time, ttl, packages_sent, packages_received, packages_lost, percent_lost_pack, min_time, max_time, avg_time]
    return result_row


list_of_domains = ["google.com", "yandex.ru", "apple.com", "microsoft.com", "amazon.com", "disney.com", "vk.com", "youtube.com", "spotify.com", "music.yandex.ru"]

with open('file.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["Domen name", "IP", "Bytes", "Time", "TTL", "Packages sent", "Packages received", "Packages lost", "Percent lost packages", "Min time", "Max time", "Average time"])
    for domain in list_of_domains:
        writer.writerow(get_ping_data(domain))
