dict = {
    "notifications": [
        {
            "ID": "724e97c3-baae-4d4f-b77b-f9e37dfc91f5",
            "Type": "Event",
            "Message": "traditional-day",
            "Timestamp": "2026-07-01 08:14:23"
        },
        {
            "ID": "7bad5ab9-f900-410c-968d-7b0b3472dc0e",
            "Type": "Event",
            "Message": "tech-fest",
            "Timestamp": "2026-07-02 00:14:07"
        },
        {
            "ID": "a89c7f0f-4b1d-490a-b813-86ecb1ae03e2",
            "Type": "Result",
            "Message": "mid-sem",
            "Timestamp": "2026-07-02 02:43:51"
        },
        {
            "ID": "580c0677-cefe-47e3-a60f-028f189b22a3",
            "Type": "Placement",
            "Message": "Microsoft Corporation hiring",
            "Timestamp": "2026-07-01 07:43:35"
        },
        {
            "ID": "0a9a49e7-0b3b-4885-82b2-7ccfd441694f",
            "Type": "Result",
            "Message": "mid-sem",
            "Timestamp": "2026-07-01 18:43:19"
        },
        {
            "ID": "7cb86d1e-1d41-4a19-b3cb-24ababbc53f8",
            "Type": "Placement",
            "Message": "Apple Inc. hiring",
            "Timestamp": "2026-07-01 23:43:03"
        },
        {
            "ID": "e6e124ea-f96c-438c-848a-c9162e43f4a6",
            "Type": "Result",
            "Message": "internal",
            "Timestamp": "2026-07-01 20:42:47"
        },
        {
            "ID": "de6c4b06-81c1-476b-aabe-ae1b03628c76",
            "Type": "Result",
            "Message": "project-review",
            "Timestamp": "2026-07-01 12:42:31"
        },
        {
            "ID": "c4ff9bec-fdfc-4546-abea-a262b34acba2",
            "Type": "Event",
            "Message": "traditional-day",
            "Timestamp": "2026-07-01 06:42:15"
        },
        {
            "ID": "fe06e628-8bc6-4279-9131-e9518363af33",
            "Type": "Result",
            "Message": "mid-sem",
            "Timestamp": "2026-07-01 23:11:59"
        },
        {
            "ID": "a5ed1185-25a8-42bb-8bbb-28705c66b190",
            "Type": "Result",
            "Message": "external",
            "Timestamp": "2026-07-02 05:11:43"
        },
        {
            "ID": "21421681-e1d5-4062-bf3e-d9485d0048d0",
            "Type": "Placement",
            "Message": "PayPal Holdings Inc. hiring",
            "Timestamp": "2026-07-01 21:41:27"
        },
        {
            "ID": "00a7e897-0b3f-49a4-91ca-704c38e31bb3",
            "Type": "Placement",
            "Message": "Marvell Technology Inc. hiring",
            "Timestamp": "2026-07-01 20:41:11"
        },
        {
            "ID": "69791e05-2342-4cbd-a2b7-593970d7bd78",
            "Type": "Result",
            "Message": "project-review",
            "Timestamp": "2026-07-02 00:10:55"
        },
        {
            "ID": "fff3e93a-2d89-4ee7-9f9d-ccf1820c3116",
            "Type": "Result",
            "Message": "external",
            "Timestamp": "2026-07-01 17:40:39"
        },
        {
            "ID": "4e47a412-a8b7-4577-94c0-b5d95404cf85",
            "Type": "Placement",
            "Message": "Advanced Micro Devices Inc. hiring",
            "Timestamp": "2026-07-01 09:10:23"
        },
        {
            "ID": "01cb5bf3-7c75-4c0d-8fd0-ebe8e6e13ba1",
            "Type": "Result",
            "Message": "project-review",
            "Timestamp": "2026-07-01 15:10:07"
        },
        {
            "ID": "2060b53a-82bd-48bd-9052-8f4a4dd99e55",
            "Type": "Result",
            "Message": "end-sem",
            "Timestamp": "2026-07-01 18:39:51"
        },
        {
            "ID": "f2836602-cf38-4feb-ab5c-6e80c64b14a3",
            "Type": "Result",
            "Message": "external",
            "Timestamp": "2026-07-02 05:09:35"
        },
        {
            "ID": "27181146-a7dc-4c02-9a91-39aea0726a6d",
            "Type": "Result",
            "Message": "project-review",
            "Timestamp": "2026-07-01 20:09:19"
        }
    ]
}
for notification in dict["notifications"]:
    if notification["Type"] == "Placement":
        print(f"placement notification: {notification['Message']} at {notification['Timestamp']}") 
    elif notification["Type"] == "Result":
        print(f"result notification: {notification['Message']} at {notification['Timestamp']}")
    elif notification["Type"] == "Event":
        print(f"event notification: {notification['Message']} at {notification['Timestamp']}")

