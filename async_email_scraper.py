import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import re

reg_nos = []


# Add all possible registration numbers between two values
def add_reg_nos(first_index, second_index, third_index_start, third_index_end):
    for x in range(int(third_index_start), int(third_index_end)+1):
        if x < 10:
            reg_nos.append(f"{first_index}-{second_index}-000"+f"{x}")
        if x > 10 and x < 100:
            reg_nos.append(f"{first_index}-{second_index}-00"+f"{x}")
        if x > 100:
            reg_nos.append(f"{first_index}-{second_index}-0"+f"{x}")


emails = []


# Check if an email exists for given registration number and add it to the list
async def add_email(reg_no):
    async with ClientSession() as session:
        async with session.get("http://www.contactopyme.gob.mx/integradoras/"
                               f"DirectorioB.Asp?CsRegistro={reg_no}") as res:
            try:
                text = await res.text()
                soup = BeautifulSoup(text, 'html.parser')
                elems = soup.select("b")

                email = re.match("<b>(.+@.+)</b>", str(elems[26]))
                if email is not None:
                    print(str(email.groups()[0]))
                    emails.append(email.groups()[0])
            except Exception:
                pass


async def main():
    for reg_no in reg_nos:
        await add_email(reg_no)

add_reg_nos("01", "001", "5", "34")
add_reg_nos("02", "001", "1", "30")
add_reg_nos("02", "002", "1", "46")
add_reg_nos("03", "001", "1", "16")
add_reg_nos("04", "001", "1", "14")
add_reg_nos("05", "001", "2", "13")

add_reg_nos("05", "003", "2", "19")
add_reg_nos("06", "001", "4", "8")
add_reg_nos("07", "001", "1", "28")
add_reg_nos("07", "002", "1", "11")
add_reg_nos("08", "001", "5", "25")
add_reg_nos("08", "002", "1", "15")

add_reg_nos("09", "001", "3", "143")
add_reg_nos("10", "001", "1", "17")
add_reg_nos("10", "002", "1", "9")
add_reg_nos("11", "001", "1", "44")
add_reg_nos("11", "002", "1", "41")
add_reg_nos("12", "001", "2", "20")

add_reg_nos("12", "002", "1", "8")
add_reg_nos("13", "001", "1", "19")
add_reg_nos("14", "001", "5", "108")
add_reg_nos("15", "001", "8", "25")
add_reg_nos("16", "001", "2", "54")
add_reg_nos("17", "001", "5", "20")

add_reg_nos("18", "001", "1", "31")
add_reg_nos("19", "001", "2", "50")
reg_nos.append("19-001-055")
add_reg_nos("20", "001", "1", "85")
add_reg_nos("21", "001", "2", "36")
add_reg_nos("22", "001", "6", "27")
add_reg_nos("23", "001", "7", "15")

add_reg_nos("23", "002", "3", "7")
add_reg_nos("24", "001", "4", "25")
add_reg_nos("25", "001", "1", "140")
add_reg_nos("26", "001", "4", "30")
add_reg_nos("26", "002", "1", "18")
add_reg_nos("17", "001", "5", "20")
reg_nos.append("26-004-0002")

add_reg_nos("27", "001", "2", "17")
add_reg_nos("28", "001", "8", "9")
add_reg_nos("28", "002", "2", "7")
reg_nos.append("28-003-0001")
add_reg_nos("28", "004", "3", "10")
add_reg_nos("28", "005", "1", "10")
add_reg_nos("29", "001", "2", "9")

add_reg_nos("30", "001", "1", "54")
add_reg_nos("30", "002", "4", "54")
add_reg_nos("30", "003", "1", "40")
add_reg_nos("30", "004", "2", "19")
add_reg_nos("31", "001", "2", "29")
add_reg_nos("32", "001", "3", "28")

reg_nos.append("99-0007-08")
reg_nos.append("99-0008-02")
reg_nos.append("99-0010-18")
reg_nos.append("99-0013-32")
reg_nos.append("99-0016-30")
reg_nos.append("99-0022-14")
reg_nos.append("99-0023-25")
reg_nos.append("99-0045-08")
reg_nos.append("99-0049-21")
reg_nos.append("99-0050-21")
reg_nos.append("99-0067-21")
reg_nos.append("99-0074-21")
reg_nos.append("99-0075-30")

reg_nos.append("99-0078-08")
reg_nos.append("99-0087-28")
reg_nos.append("99-0091-08")
reg_nos.append("99-0092-17")
reg_nos.append("99-0101-08")
reg_nos.append("99-0106-08")
reg_nos.append("99-0110-08")
reg_nos.append("99-0112-17")
reg_nos.append("99-0116-08")
reg_nos.append("99-0117-02")
reg_nos.append("99-0123-09")
reg_nos.append("99-0124-02")
reg_nos.append("99-0136-09")

reg_nos.append("99-0139-15")
reg_nos.append("99-0142-25")
reg_nos.append("99-0160-07")
reg_nos.append("99-0161-01")
reg_nos.append("99-0162-09")
reg_nos.append("99-0163-15")
reg_nos.append("99-0164-09")
reg_nos.append("99-0165-05")
reg_nos.append("99-0166-05")
reg_nos.append("99-0167-03")
reg_nos.append("99-0168-26")
reg_nos.append("99-0169-08")
reg_nos.append("99-0170-02")

asyncio.run(main())
with open("emails.txt", "w") as file:
    file.write("\n".join(email for email in emails))
