import pytest
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Iniciar o WebDriver usando GeckoDriver
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")

def test_check_title_is(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    # Verifica se o titulo de página é
    sleep(5)
    # Capturar o título da página
    page_title = driver.title

    # Verificar se o título da página é o esperado
    expected_title = "Validador de schema excel"  # Substitua com o título real esperado
    assert page_title == expected_title, f"O título da página era '{page_title}', mas esperava-se '{expected_title}'"

def test_check_streamlit_h1(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(5)  # Espera 5 segundos

    # Capturar o primeiro elemento <h1> da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> é o esperado
    expected_text = "Insira o seu excel para validação"
    assert h1_element.text == expected_text

def test_check_usuario_pode_inserir_um_excel_e_receber_uma_mensagem(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(5)  # Espera 5 segundos

    # Realizar o upload do arquivo de sucesso
    success_file_path = os.path.abspath("data/arquivo_excel.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

    # Aguardar a mensagem de sucesso
    sleep(5)
    assert "O schema do arquivo Excel está correto!" in driver.page_source

def test_failed_upload(driver):
    driver.get("http://localhost:8501")

    # Aguardar um tempo para a aplicação carregar
    sleep(5)

    # Realizar o upload do arquivo de falha
    failure_file_path = os.path.abspath("data/failure.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(failure_file_path)

    # Aguardar a mensagem de erro
    sleep(5)
    assert "Erro na validação" in driver.page_source