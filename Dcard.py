from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re


PATH = "/Users/enjuichang/chromedriver"
driver = webdriver.Chrome(PATH)


URLs = [
    [
        "https://www.pttbrain.com/dcard/forum/c332e370-8d22-4b07-80ce-f27a93872962",
        "https://www.pttbrain.com/dcard/forum/9b5213d6-4427-4a3c-b788-efa19493631c",
        "https://www.pttbrain.com/dcard/forum/8a2a0b9a-7664-49b0-bff7-58389ef73a0d",
        "https://www.pttbrain.com/dcard/forum/214c3abb-6cf8-44b2-86b3-c156a9c5bbf2",
        "https://www.pttbrain.com/dcard/forum/d55a7e9f-95c0-41d3-8890-964e233e36a7",
        "https://www.pttbrain.com/dcard/forum/4ccb34a2-4d78-4ec0-8287-b6006c9087f6",
        "https://www.pttbrain.com/dcard/forum/8e21e2e3-1e7a-42e4-86bb-0b15d034b634",
        "https://www.pttbrain.com/dcard/forum/2ec9978e-181c-4e14-8ada-18533d1e3d45",
        "https://www.pttbrain.com/dcard/forum/79b1968a-3d30-43b9-b413-1977725cf7f0",
        "https://www.pttbrain.com/dcard/forum/863b960a-72a8-4479-80a2-b976275c002e"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/f8acd3e6-17e9-4d9d-bc7c-bf24d94c2ad1",
        "https://www.pttbrain.com/dcard/forum/e0a290f4-752b-48a2-a791-f211f8b46588",
        "https://www.pttbrain.com/dcard/forum/d0cd5819-4627-4b5f-8a8e-050976e0fba1",
        "https://www.pttbrain.com/dcard/forum/fb66dd2c-8b39-4bc0-a7a5-29bca6b215af",
        "https://www.pttbrain.com/dcard/forum/8a2a5245-984b-4757-9c08-eee91a539153",
        "https://www.pttbrain.com/dcard/forum/ba0145a2-adff-4229-9a84-9b26ebd2f7f0",
        "https://www.pttbrain.com/dcard/forum/97eb486d-2f9d-4912-8b5d-b8f539e449d4",
        "https://www.pttbrain.com/dcard/forum/3d5ea668-ec42-458c-91bb-12fa8e9afa27"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/6eeeafb2-9dac-4d81-ae4b-ffecf0ad4444",
        "https://www.pttbrain.com/dcard/forum/53ad45b4-dcef-479a-8c3e-a9e97527b2a4",
        "https://www.pttbrain.com/dcard/forum/45a2cade-341a-4d5d-a1d8-b1cf82f77277",
        "https://www.pttbrain.com/dcard/forum/960b42f9-9dc3-483e-829f-466be52d2906",
        "https://www.pttbrain.com/dcard/forum/a5837b3c-088c-45a0-b537-28f91ce83c63",
        "https://www.pttbrain.com/dcard/forum/834c3634-e023-4189-a2fd-3c2cc47133e4",
        "https://www.pttbrain.com/dcard/forum/9d18b308-26f5-4239-960b-df60f81175c7",
        "https://www.pttbrain.com/dcard/forum/4fb1cbbf-57e3-46d0-9242-eb99fc0beea8",
        "https://www.pttbrain.com/dcard/forum/b3c0adaa-88e0-4342-8184-7320680c3c0e",
        "https://www.pttbrain.com/dcard/forum/1d909998-c33f-4556-8685-63e507cdc853"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/b5b2653a-6304-4564-9ea0-a4cec0be7aee",
        "https://www.pttbrain.com/dcard/forum/c177f426-2627-4050-b989-eedc3371e610",
        "https://www.pttbrain.com/dcard/forum/3927a13e-67e8-4a3b-b271-dea8048a0129",
        "https://www.pttbrain.com/dcard/forum/49eed176-a7ad-492c-b6cf-77733ab633ef",
        "https://www.pttbrain.com/dcard/forum/26e4252c-63d8-401b-82a9-110fe1e306db"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/be1a095b-175e-4523-9e06-66a05d939676",
        "https://www.pttbrain.com/dcard/forum/cbd5285f-3cba-4bfc-86d0-1ab52d201459",
        "https://www.pttbrain.com/dcard/forum/5b964198-2e59-419d-b44c-0276d0fea7e8",
        "https://www.pttbrain.com/dcard/forum/1a14ba93-3989-47e5-aedc-a3918963100e",
        "https://www.pttbrain.com/dcard/forum/d7db42a8-bedb-4ea2-96a7-c9034f4dd89a",
        "https://www.pttbrain.com/dcard/forum/817d71bb-ebdf-4326-b8aa-10df4fcdf03a",
        "https://www.pttbrain.com/dcard/forum/d5ee9d02-510e-4f81-96e9-ab59b56e21ca",
        "https://www.pttbrain.com/dcard/forum/4736baba-5375-40b6-8a1b-f3a24be6bf24",
        "https://www.pttbrain.com/dcard/forum/6abae5c6-33c2-463d-9629-d4432662c9ab",
        "https://www.pttbrain.com/dcard/forum/23082c2f-c19d-456c-a805-1e6ac0a36c31",
        "https://www.pttbrain.com/dcard/forum/70c4b5d1-055e-48a7-b874-2c9dace6e4d6",
        "https://www.pttbrain.com/dcard/forum/de977130-f3eb-467b-822e-b0e91124e9eb",
        "https://www.pttbrain.com/dcard/forum/6120536f-6a70-49bb-8891-ec0ba2f4b396",
        "https://www.pttbrain.com/dcard/forum/a255fb97-4199-4bd0-9b28-1ec2c0d2f382"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/d43f33f9-873f-46b3-9f24-38c90056b96c",
        "https://www.pttbrain.com/dcard/forum/ecc6a486-c4ac-4f76-996d-7dda5dcb8518",
        "https://www.pttbrain.com/dcard/forum/cd2959fe-5515-4c1e-bd35-1cd4c36b44f0",
        "https://www.pttbrain.com/dcard/forum/6bec54a2-7dfd-46b5-8752-7781b3f91efe",
        "https://www.pttbrain.com/dcard/forum/58dba906-09c2-4808-9206-11c008c9ef16",
        "https://www.pttbrain.com/dcard/forum/2bb20844-07ec-41d3-830f-ae551fc31246"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/0e0bc27b-8c69-4149-b229-04e7a865a09d",
        "https://www.pttbrain.com/dcard/forum/a1e20a52-c15e-42a2-980d-7401cfab4df7",
        "https://www.pttbrain.com/dcard/forum/ab9d18b6-f990-410a-8cf8-4dbb34f084fa",
        "https://www.pttbrain.com/dcard/forum/19202aff-7a81-4da6-bc02-cc0ad07a13e7",
        "https://www.pttbrain.com/dcard/forum/577f29b9-ef96-4e05-9e79-55e2a7d6e3db",
        "https://www.pttbrain.com/dcard/forum/3ec80bb0-2f02-478f-9afd-711327b460c5"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/42851318-b9e2-4a75-8a05-9fe180becefe",
        "https://www.pttbrain.com/dcard/forum/75a726e6-d4e3-4902-a410-2430a39fffcb",
        "https://www.pttbrain.com/dcard/forum/c1f60d65-4f49-4a56-9c00-f162c93e31a9",
        "https://www.pttbrain.com/dcard/forum/d5f84f54-2ac2-42a2-96b1-de3d8c409b8b"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/fc7574ad-e1df-43d2-bb06-8825c718c065",
        "https://www.pttbrain.com/dcard/forum/6ea32129-c485-4321-9030-f7f45ae4cc2f"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/3bceb81c-574e-4a96-8050-4df56096d0df",
        "https://www.pttbrain.com/dcard/forum/2fb88b62-aa28-4b18-af51-dda08dd037a9",
        "https://www.pttbrain.com/dcard/forum/5f5d5f53-584d-4871-b6f0-afe8c24ce37e",
        "https://www.pttbrain.com/dcard/forum/e91644fb-5a42-42e0-9526-61b1e133559d",
        "https://www.pttbrain.com/dcard/forum/638dede9-28ab-4288-9552-8345e4dbf9a8"
    ],
    [
        "https://www.pttbrain.com/dcard/forum/72f262c4-75aa-4d75-ab0e-cd7bd09e69b5",
        "https://www.pttbrain.com/dcard/forum/ea38435a-1533-4eb0-9c66-76451d31fc35",
        "https://www.pttbrain.com/dcard/forum/938bcf31-3da6-4b3c-83b0-78cf9ad6dbbe",
        "https://www.pttbrain.com/dcard/forum/b5bffbd7-da4f-4591-8323-e763b3accf4d",
        "https://www.pttbrain.com/dcard/forum/14185ae6-44ab-45e2-88da-ae97e0159c9f",
        "https://www.pttbrain.com/dcard/forum/bd5f5b7c-5bb1-4a99-8e01-6c4e3451dd64",
        "https://www.pttbrain.com/dcard/forum/06239f5b-6fbc-4159-bfa3-73defacf1c0a",
        "https://www.pttbrain.com/dcard/forum/977976c6-d4b7-4163-83d5-010c32ed46cd",
    ],
    [
        "https://www.pttbrain.com/dcard/forum/b7db78c7-7b32-4da5-a565-907a892259d7",
        "https://www.pttbrain.com/dcard/forum/0a859162-88d8-4406-8111-71c57aae84a1",
        "https://www.pttbrain.com/dcard/forum/9e4476fc-d1b4-4490-a578-fc4dc95ffc52",
        "https://www.pttbrain.com/dcard/forum/6cf320df-3f3a-495f-9764-3dfbef767c49",
        "https://www.pttbrain.com/dcard/forum/14f573f5-3f02-4821-8e18-f561d7b7db91",
        "https://www.pttbrain.com/dcard/forum/f0c59f55-18bb-4190-a15a-a5413ca9fa9d",
        "https://www.pttbrain.com/dcard/forum/2e57a052-affa-4b32-a68d-98d7d6020c12"
    ]
]

labelLIST = ["運動","藝文","職場","議題","生活","教育","科技","情感","時事","財經","ACG","娛樂"]

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def extractTitle(string):
    str_compiler = re.compile('\\n+.+')
    replaceParts = str_compiler.findall(string)
    for i in replaceParts:
        string = string.replace(i," ")
    return string

def extractContent(string):
    str_compiler = re.compile(r'https?://\S+|www\.\S+')
    replaceParts = str_compiler.findall(string)
    for i in replaceParts:
        for j in i:
            string = string.replace(j,"")
    return string


titles = []
contents = []

for k in range(len(URLs)):
    id = labelLIST[k]
    for j in range(len(URLs[k])):
        driver.get(URLs[k][j])
        for i in range(40):
                for i in range(1,6):
                    xpath = "//div[@class='ui container'][4]/div[@class='ui attached segment']/div[@class='ui large animated divided selection relaxed list']/a[@class='item']["+str(i)+"]"
                    page = WebDriverWait(driver,10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    page.click()
                    title = WebDriverWait(driver,10).until(
                            EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='ui left floated header']"))
                        )
                    
                    content = driver.find_element_by_xpath("//p/div[@class='blurring dimmable']/span")


                    titles.append(id)

                    header = extractTitle(title[0].text)
                    text = extractContent(content.text)
                    text = text.replace("\n"," ").replace("   ","").replace("#","").replace("-------","").replace("…","").replace("(ì _ í)","").replace("🥲","").replace("⋯⋯","").replace("....","").replace(" / ","").replace("ಥ_ಥ","").replace(">","").replace("<","").replace("“","").replace("”","").replace("~","")
                    contents.append(header+" "+text)
                    print(id,header+" "+text)
                    driver.back()
                
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "⟩"))).click()
                #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui pagination menu']/a[@aria-label='Next item']"))).click()


print("Succeed")
driver.quit()
outputDF = pd.DataFrame({"id": titles,"content":contents})
outputDF.to_csv("dcard/CSV/dcard.csv")
