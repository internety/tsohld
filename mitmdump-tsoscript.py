
import os
from mitmproxy import http
tso_cdn_hosts = [ 'static.cdn.ubi.com', \
                  'static10.cdn.ubi.com', \
                  'static13.cdn.ubi.com', \
                  'static14.cdn.ubi.com', \
                  'ubistatic-a.akamaihd.net' ]

def check_string(string, substring_list):
    for substring in substring_list:
        if substring in string:
            return True
    return False

def request(self, flow):
    flow.request.anticache()
    flow.request.anticomp()

def response(flow):
    if flow.request.pretty_host in tso_cdn_hosts:
        if check_string(flow.request.pretty_url,
        ["00ec9136d6ff4fedc70cdaa37a3bb25c4f4ab1e2",
        "d1d8cf6dcf7597f57377a3b028307fb54d5678d8",
        "30f0baaaa12e4447144153f46136b449dd3c3b75",
        "d8bcb64f81ea66d2bb405a76352d1e54bf51ee0b",
        "dc81f60a9758824be51adf5523863d318b9a7142",
        "144e19ee3f16e12972695cea95ba2024b9dec3cf",
        "c55f730b452e9ac32a2fa2de53f71493712a2db5",
        "6d11dcde93afce91bc146f88e622f450201e4fff",
        "91cc31f70b5c84a1a8f7882b93947c8ffcf44988",
        "18704a048ab2e8da9b94bca25b9b7b6b1dce817c",
        "1f49e02e088178d0aa7483135784ae22555c52b9",
        "270c6c638bcbe5113fbe0589b8e25b136782c01d",
        "14c7944b896b543eb00773e83b451f6032d9566e",
        "a64bb599de5b4cff09cf5d93f68db2d563a7cf39",
        "ce8c87f1da7663e716162c2dcd43b1504e08fa93",
        "4a2c4c60a0fc0e8320ae43afd0a60f52acf6fe35",
        "84e216219729c2f916780a3b80950bc5afe0725e",
        "ff2bd6901dd57d55a5a7a7f5d632ee4e2e9a15d6",
        "266a7e26836bc830512cd0ea919481562a0009df",
        "a5f5d240cff9ff0e625eef02d7d926dc0ee92a63",
        "7dc1e1f289646ba15aeef107efe7026ebb58e8b1",
        "1dd24082bcd22fc20777357499e2394897e2a37a",
        "df8a33947846c9f8ce2f2902a0cdba4adf8b7b48",
        "4879d59fc8fa0ce0ba5e87b4c34031f2e16ca5f9",
        "0c1d43eea8d2e74ab52103c30e3ac2f6eea5dd91",
        "5a204d4374fefad3d55858a62850c81804f18978",
        "5621cbed3a6b20791e0439123b8231b459a668ea",
        "31437bd8393e7b6c386bc72f045530009e09b50c",
        "85ce87088f887aed36f7d4b1ee2b423c82b30a99",
        "d5de5a5369c541c8b9f1d2efe2a3a7d5b7acd4cb",
        "ab5333c0dc06caddc500444d976132936aa98eab",
        "1515f7c8c753cc379ea7056062297f92d5ccfe85",
        "41b8238caac031c265efe08544a21ac4be91f534",
        "0a1384a56afe4f1469fe2f2ea87a0e1cd0c3af64",
        "11fa4311ceabae96ac58b954921b2930f82724c2",
        "f9194a1613b2c3db8b383d87c86d6e100d8ac905",
        "f237f6c7e3b6c6aac01ae7f51cd917bdeb6ddec2",
        "5411ec93e61930e6eb3a958c56b81ba63023a9ee",
        "bd76cd8196c23aaf73139bc263002cf759afc1ce",
        "8257a3e50f6ae19db4aeb2c978949b2d81021a61",
        "a761cd0aeca1a908ee28c76f882fb3970178f7cf",
        "77ea4e96f3a2fbe1a73a5cfe6892fa1fc5343d51",
        "3da48a638753a4f5c846a433d6f984e25bb0954c",
        "29e687a31e953020cf937c36a8fa5036793b89ec",
        "d8c8060e31406770e71c5c6557f1873c2e424920",
        "4afb3220ff0e36afab7a0fcb6368c1c064885178",
        "2f723e660a18567097b0353bb1b968b68235cf80",
        "ae018b91595f76a6ced714a49c185314ff545576",
        "62b89f4ed680ca42fff2ffb9273131867c97856c",
        "cca4d11ec41b5976e2e13e6c945bb07b96f656ba",
        "db5c26a467c4f5dee9804c7c88417103515c326a",
        "1360edb7f0ac34e79ebb45785a22fc487b12133f",
        "db81ed6ff478e21963acf22482e82c714de22afb",
        "b6f18650709206e1cb1f66667a7e23f54876ec8a",
        "3d3374986078b177592918eb8bcf6864c163b81d",
        "cd9826b00ff6eef4d108a443c08d80963619b408",
        "47f70a26b1d41942a146b4bd85fa08c6f9eb507a",
        "1170eb8a879b4cd707fb8f06db692e88d731e72b",
        "edf8a4990c5f62ee7572224cc8aa2f054d7d70d8",
        "a0c80b2be9f9ac18fa000aac21424cdfceb5b8eb",
        "897e62c01ab92c96534bda8db45ef14f5bf4afe2",
        "9cbc282c345ca985e8b4c06fff0b70c1c401333e",
        "391f27161838c932f5786d28737ab71a3d124026",
        "eb4cb901ba6db7647bfd3bc6979fa625207da742",
        "4485f4b09a5c75e0334b626d624442fcd0cb95e1",
        "c49d861fba55129a99cd95d7ed805583253ae7e9",
        "6ae32e11fd1e08a78777ce73e04840351ef9c046",
        "a8b71035ad6c181b765b26760339c0007ca3a4b7",
        "d07bd52c704baea8add876c60963b5a5db61f8fe",
        "ec4086d28159117f18ecdc550ec2e4527eb1d256",
        "cc267708e034cdc4cf898534b345b27493a8e6c1",
        "00ec9136d6ff4fedc70cdaa37a3bb25c4f4ab1e2",
        "b811bfd138c45038e9a6fed17bb6e218578b9f21",
        "178dd055437b153c791b3bbc17b1bc573def9f3b",
        "25c50173bf78b34015c74d267381e9b7f5f62358",
        "99c8270858fab5b115c480b4951b575c2bb5e45f",
        "c60d9778a111ad94a43ada4763afcc16aeb76b58",
        "b195e41557f4ddfdcc9a0a4615019b129a0aae7a",
        "9367d4b213d89c1ac68628cffe8821301f16d7c9",
        "76ddf11ab2b648507adb57667e03ee175145c0eb",
        "165b87dddda22a5608c462a548858a82647ac78f"]):
            img = open("herbs.png", "rb").read()
            flow.response.content = img
            flow.response.headers["Content-Type"] = "image/png"
            flow.response.headers["Content-Length"] = "4151"
            print("replace png: " + flow.request.pretty_url)  


        if check_string(flow.request.pretty_url,
        ["3622a4b2282f27f86977e95fc9a8dcdecbc0f577",
        "0a3b0c84b23f14bdecedf23e0c66d221807d71f6"]):
            pack = open("pack.bin", "rb").read()
            flow.response.content = pack
            flow.response.headers["Content-Length"] = "328100"
            print("replace bin: " + flow.request.pretty_url)

#        if check_string(flow.request.pretty_url,["crossdomain.xml"]):
#            xml = open("crossdomain.xml", "rb").read()
#            flow.response.content = xml
#            print("replace xml: "+flow.request.pretty_url)
