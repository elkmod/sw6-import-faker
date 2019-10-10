# Data faker script

import sys

from faker import Faker
from faker.providers import company, internet
import uuid
import random

# Parameter initialization
# init.py [limit-products] [limit-categories] [limit-manufacturers]
LIMIT_PROD = int(sys.argv[1]) or 10
LIMIT_CATE = int(sys.argv[2]) or 10
LIMIT_MANU = int(sys.argv[3]) or 10

CURRENCY_ID = 'b7d2554b0ce847cd82f3ac9bd1c0dfca'
SALES_CHANNEL_ID = '59448ae2b0a2496d846e69247f4e1316'
CATEGORY_ID = '017bb1c4a9ee46d58a057e98a01fd678'

print('Python faker v0.1')

# Company template
template_manufacturer = """{{"id": "{0}","name": "{1}"}}"""
template_product = """{{"id":"{0}","name":"{1}","stock":{2},"manufacturerId":"{3}","description":"{4}","tax":{{"name":"19%","taxRate":19.0}},"price":[{{"currencyId":"{5}","gross":{6},"net":{7},"linked":true}}],"productNumber":"{8}","categories":[{{"id":"{9}"}}],"visibilities":[{{"salesChannelId":"{10}","visibility":30}}]}}"""

header_product = """INSERT INTO `product` (`id`,`version_id`,`auto_increment`,`product_number`,`active`,`parent_id`,`parent_version_id`,`tax_id`,`product_manufacturer_id`,`product_manufacturer_version_id`,`delivery_time_id`,`deliveryTime`,`product_media_id`,`product_media_version_id`,`unit_id`,`category_tree`,`option_ids`,`property_ids`,`tax`,`manufacturer`,`cover`,`unit`,`media`,`prices`,`visibilities`,`properties`,`categories`,`translations`,`price`,`listing_prices`,`manufacturer_number`,`ean`,`stock`,`available_stock`,`available`,`restock_time`,`is_closeout`,`purchase_steps`,`max_purchase`,`min_purchase`,`purchase_unit`,`reference_unit`,`shipping_free`,`purchase_price`,`mark_as_topseller`,`weight`,`width`,`height`,`length`,`release_date`,`whitelist_ids`,`blacklist_ids`,`tag_ids`,`tags`,`variant_restrictions`,`configurator_group_config`,`searchKeywords`,`created_at`,`updated_at`,`rating_average`,`display_group`,`child_count`)VALUES"""
template_product = """\n(X'{0}',X'0FA91CE3E96A4BC2BE4BD9CE752C3425',{1},'{2}',1,NULL,NULL,X'6030F5409DE049C8842CA84F9B004B3A',X'DA96C7BAE5ED41F298C09B64306488AD',X'0FA91CE3E96A4BC2BE4BD9CE752C3425',null,null,null,null,null,'["2d51bba0ec6f453090c060d97f010005"]',null,null,X'6030F5409DE049C8842CA84F9B004B3A',X'DA96C7BAE5ED41F298C09B64306488AD',null,null,X'3477B5551F644ADB91215258DC5D7462',X'3477B5551F644ADB91215258DC5D7462',X'3477B5551F644ADB91215258DC5D7462',X'3477B5551F644ADB91215258DC5D7462',X'3477B5551F644ADB91215258DC5D7462',X'3477B5551F644ADB91215258DC5D7462','{{"cb7d2554b0ce847cd82f3ac9bd1c0dfca":{{"currencyId":"b7d2554b0ce847cd82f3ac9bd1c0dfca","net":156.07,"linked":true,"gross":167}}}}',null,null,null,19,19,1,3,0,1,null,1,null,null,0,null,null,null,null,null,null,null,null,null,null,X'3477B5551F644ADB91215258DC5D7462',null,null,X'3477B5551F644ADB91215258DC5D7462','2019-09-30 13:55:46.220',null,null,'6e49140368962b4a66916349052d67dd',null)"""

fake = Faker('de_DE')
fake.add_provider(company)
fake.add_provider

manufacturers = []

# Generate manufacturers
file_stream = open('generated/manufacturer-{0}.json'.format(LIMIT_MANU), 'w+')
file_stream.write('[')
for i in range(0, LIMIT_MANU):
	m_uuid = uuid.uuid4().hex
	manufacturers.append(m_uuid)
	file_stream.write(template_manufacturer.format(m_uuid, fake.company()))
	if i < LIMIT_MANU - 1:
		file_stream.write(',')
file_stream.write(']')
file_stream.close()

# Generate categories

# Generate products
auto_increment = 1000010
batch_size = 1000

file_stream = open('generated/product-{0}.sql'.format(LIMIT_PROD), 'w+')
file_stream.write(header_product)

for i in range(0, LIMIT_PROD):

	if(i % batch_size == 0 and i != 0):
		file_stream.write(';\n')
		file_stream.write(header_product)

	p_uuid = uuid.uuid4().hex
	p_net = random.randint(1, 10000)/100
	file_stream.write(template_product.format(
		p_uuid, # uuid
		auto_increment,
		p_uuid
		))

	auto_increment = auto_increment + 1

	if((i + 1) % batch_size != 0):
		file_stream.write(',')

file_stream.close()

