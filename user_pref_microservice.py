import tkinter
from tkinter import ttk
import json
import time

while True:
    time.sleep(1)
    with open('run-micro.txt') as file:
        read_data = file.read()
        if read_data =='run':
            with open('run-micro.txt', 'w') as file:
                file.seek(0)
                file.truncate()

            window = tkinter.Tk()
            window.title("Data Entry Form")

            frame = tkinter.Frame(window)
            frame.pack()


            def enter_data():
                uid = user_id_entry.get()
                recent_urls = recent_url_entry.get()
                sport_pref = sport_pref_entry.get()
                expo_format = export_format_combobox.get()
                user_pref = {'userID': uid, 'recentUrls': recent_urls, 'sport_pref': sport_pref,
                             'exportFormat': expo_format}
                json_export = json.dumps(user_pref, indent=4)
                with open('receive-preferences.txt', 'w') as file:
                    file.write(json_export)


            # Saving User Info
            user_info_frame = tkinter.LabelFrame(frame, text="User Information")
            user_info_frame.grid(row=0, column=0, padx=20, pady=20)

            user_id_label = tkinter.Label(user_info_frame, text="UID")
            user_id_label.grid(row=0, column=0)
            recent_url_label = tkinter.Label(user_info_frame, text="Recent URLs")
            recent_url_label.grid(row=0, column=1)

            user_id_entry = tkinter.Entry(user_info_frame)
            recent_url_entry = tkinter.Entry(user_info_frame)
            user_id_entry.grid(row=1, column=0)
            recent_url_entry.grid(row=1, column=1)

            sport_pref_label = tkinter.Label(user_info_frame, text="Sport Preference")
            sport_pref_label.grid(row=0, column=2)
            sport_pref_entry = tkinter.Entry(user_info_frame)
            sport_pref_entry.grid(row=1, column=2)

            export_format = tkinter.Label(user_info_frame, text="Preferred Export Format")
            export_format_combobox = ttk.Combobox(user_info_frame, values=["Excel", "CSV", "JSON"])
            export_format.grid(row=0, column=3)
            export_format_combobox.grid(row=1, column=3)

            button = tkinter.Button(frame, text="Submit", command=enter_data)
            button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

            window.mainloop()
