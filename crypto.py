from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

prices = []


def intro():
    loading = 'Načítám aktuální kurzy za 1 BTC z českých směnáren:'
    print(loading.center(165))
    print('-' * 170)
    print('{:<50} {:<50} {:<50}'.format('| Směnárna |', '| Cena (Kč) |', '| Poplatek |'))
    print('-' * 170)


def anycoin():
    try:
        driver.get("https://www.anycoin.cz")
        wait = WebDriverWait(driver, 3)
        price = wait.until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, 'span[class="jss253"'))).text.replace(' ', '').replace(',', '.')
        name = 'Anycoin'
        price = round(float(price), 2)
        fee = round(0.0001 * price, 2)
        fees = f'Poplatek za nákup: {fee:>2} Kč'
        print(f'{name:<50}  {price:<50} {fees:<50}')
        prices.append((name, str(price)))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def simplecoin():
    try:
        driver.get("https://www.simplecoin.eu/cs")
        wait = WebDriverWait(driver, 2)
        price_element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.css-1b35v6v')))
        price = price_element.text.replace("1 BTC = ", "").replace("CZK", ".00").replace(" ", "")
        name = 'Simplecoin'
        fee = 'Poplatek za nákup: Zahrnut v ceně'
        print(f'{name:<50}  {price:<50} {fee:<50}')
        prices.append((name, price))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def freecoin():
    try:
        driver.get("https://www.freecoin.cz")
        name = 'Freecoin'
        wait = WebDriverWait(driver, 2)
        price = wait.until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, 'span[data-direction="buy"]'))).text.replace(" ", "").replace(",", ".")
        fee = 'Poplatek za nákup: Neuveden'
        price = price.replace("Kč", "")
        print(f'{name:<50}  {price:<50} {fee:<50}')
        prices.append((name, price))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def bitbeli():
    try:
        driver.get("https://www.bitbeli.cz/#vice-informaci")
        time.sleep(4)
        price = driver.find_element(
            By.CSS_SELECTOR, 'div[class="rate_text"]').text.replace("CZK", "").replace(",", ".").replace(" ", "")
        fee = float(0.00015) * float(price)
        fee = round(fee, 2)
        fees = f'Poplatek za nákup: {fee} Kč + 2.5 % z investované částky'
        name = 'Bitbeli'
        print(f'{name:<50}  {price:<50} {fees:<50}')
        prices.append((name, str(price)))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def kriptomat():
    try:
        driver.get("https://kriptomat.io/cs/kurzy-kryptomen/")
        time.sleep(2)
        price = driver.find_element(By.CSS_SELECTOR, 'span[class="pr"]').text.replace(",", "")
        name = 'Kriptomat'
        fee = 'Poplatek za nákup: Min. 1.45EUR nebo 0.45 % z investované částky Kč'
        print(f'{name:<50}  {price:<50} {fee:<50}')
        prices.append((name, price))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def mycoiner():
    try:
        driver.get("https://www.mycoiner.cz/cs/rates")
        wait = WebDriverWait(driver, 2)
        price = wait.until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, 'p[class="text ts-18 ts-md-38 tw-500"]'))).text.replace("CZK", "").replace(" ", "")
        fee = 'Poplatek za nákup: 1.5% z investované částky'
        name = 'Mycoiner'
        print(f'{name:<50}  {price:<50} {fee:<50}')
        prices.append((name, price))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def virtual_property():
    try:
        driver.get("https://www.virtualproperty.cz")
        time.sleep(2)
        price = driver.find_element(By.CLASS_NAME, 'card-body').text
        price = round(float(price.replace(" ", "").replace("Kč", "").split()[0]), 2)
        fee = 'Poplatek za nákup: 2% z investovaná částky, min. 20 Kč'
        name = 'Virtual Property'
        print(f'{name:<50}  {price:<50} {fee:>50}')
        prices.append((name, str(price)))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def coinmate():
    try:
        driver.get("https://coinmate.io/cs/prices")
        wait = WebDriverWait(driver, 2)
        price = wait.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
        price = wait.until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, 'td[class="cdk-cell desktop-only cdk-column-price"]'))).text.replace(" ", "")\
            .replace("Kč", "").replace(",", ".")
        fee = 'Poplatek za nákup: od 0.07 do 0.35 % z investované částky'
        name = 'Coinmate'
        print(f'{"Coinmate směnárna":<50}  {price:<50} {fee:<50}')
        prices.append((name, price))
    except ValueError:
        print("Nepodařilo se načíst stránku. Nepodařilo se převést na očekávaný typ, stránka vyžaduje více času.")
    except TimeoutError:
        print("Nepodařilo se načíst stránku. Webdriver nenašel požadovaný element v rámci stanovené doby.")
    except ConnectionError:
        print("Nepodařilo se načíst stránku. Chyba spojení internetu.")
    except WebDriverWait:
        print("Nepodařilo se načíst stránku. Neplatný ovladač webového prohlížeče.")


def main():

    intro()
    anycoin()
    simplecoin()
    freecoin()
    bitbeli()
    kriptomat()
    mycoiner()
    virtual_property()
    coinmate()

    driver.quit()

    print('-' * 170)

    sorted_prices = sorted(prices, key=lambda x: x[1])
    print(f'Nejnižší cenu má směnárna {sorted_prices[0][0]} cena: {sorted_prices[0][1]} + poplatky')

    difference = float(sorted_prices[-1][1]) - float(sorted_prices[0][1])
    print(f'Rozdíl mezi nejdražší směnárnou {sorted_prices[-1][0]} '
          f'a nejlevnější {sorted_prices[0][0]} je: {round(difference, 2)} Kč + poplatky')


if __name__ == '__main__':
    main()
