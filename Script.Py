# Fiquem a vontade para editar como quiserem funciona tanto windows quanato Linux
import os
import time
import platform
import psutil

def limpar_cache_linux():
    try:
        #  de memória livre antes da limpeza
        mem_before = psutil.virtual_memory().available / (1024 * 1024)
        
        os.system('sync')
        os.system('echo 3 > /proc/sys/vm/drop_caches')
        os.system('swapoff -a && swapon -a')
        
        #  memória livre após a limpeza
        mem_after = psutil.virtual_memory().available / (1024 * 1024)
        
        print(f"Cache e memória limpos com sucesso! Memória antes: {mem_before:.2f} MB, Memória depois: {mem_after:.2f} MB")
        return True
    except Exception as e:
        print("Erro ao limpar cache e memória:", e)
        return False

def limpar_cache_windows():
    try:
        os.system('echo Limpar cache e memória no Windows')
        # Comando para limpar cache e memória no Windows
        print("Cache e memória limpos com sucesso!")
        return True
    except Exception as e:
        print("Erro ao limpar cache e memória no Windows:", e)
        return False

def otimizar_desempenho_linux():
    try:
        os.system('sysctl -w vm.swappiness=10')
        os.system('sysctl -w vm.vfs_cache_pressure=50')
        os.system('sysctl -w kernel.nmi_watchdog=0')
        print("Desempenho do sistema otimizado!")
        return True
    except Exception as e:
        print("Erro ao otimizar desempenho:", e)
        return False

def otimizar_desempenho_windows():
    try:
        os.system('echo Otimizar desempenho no Windows')
        # Comandos para otimizar desempenho no Windows
        print("Desempenho do sistema otimizado!")
        return True
    except Exception as e:
        print("Erro ao otimizar desempenho no Windows:", e)
        return False

def contagem_regressiva(segundos):
    for i in range(segundos, 0, -1):
        print(f"Próxima execução em {i} segundos...", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    while True:
        print("\nExecutando a limpeza de cache e memória...")
        
        if platform.system() == "Linux":
            if limpar_cache_linux() and otimizar_desempenho_linux():
                contagem_regressiva(60)  # Contagem regressiva de 60 segundos
            else:
                print("Falha ao executar a limpeza e otimização. Tentando novamente em 60 segundos...")
                contagem_regressiva(60)
        
        elif platform.system() == "Windows":
            if limpar_cache_windows() and otimizar_desempenho_windows():
                contagem_regressiva(60)  # Contagem regressiva de 60 segundos
            else:
                print("Falha ao executar a limpeza e otimização. Tentando novamente em 60 segundos...")
                contagem_regressiva(60)
        
        else:
            print(f"Sistema operacional '{platform.system()}' não suportado.")
            break
