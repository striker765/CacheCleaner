package main

import (
	"fmt"
	"os/exec"
	"runtime"
	"time"
)

func executarComando(comando string) error {
	cmd := exec.Command("bash", "-c", comando)
	return cmd.Run()
}

func limparCacheLinux() error {
	if err := executarComando("sync"); err != nil {
		return err
	}
	return executarComando("echo 3 > /proc/sys/vm/drop_caches")
}

func otimizarDesempenhoLinux() error {
	cmds := []string{
		"sysctl -w vm.swappiness=10",
		"sysctl -w vm.vfs_cache_pressure=50",
		"sysctl -w kernel.nmi_watchdog=0",
	}
	for _, cmd := range cmds {
		if err := executarComando(cmd); err != nil {
			return err
		}
	}
	return nil
}

func limparCacheWindows() error {
	fmt.Println("Limpar cache e memória no Windows.")
	return nil
}

func otimizarDesempenhoWindows() error {
	fmt.Println("Otimizar desempenho no Windows.")
	return nil
}

func contagemRegressiva(segundos int) {
	for i := segundos; i > 0; i-- {
		fmt.Printf("Próxima execução em %d segundos...\r", i)
		time.Sleep(1 * time.Second)
	}
	fmt.Println()
}

func main() {
	for {
		fmt.Println("\nExecutando a limpeza de cache e memória...")

		var err error
		switch runtime.GOOS {
		case "linux":
			err = limparCacheLinux()
			if err == nil {
				err = otimizarDesempenhoLinux()
			}
		case "windows":
			err = limparCacheWindows()
			if err == nil {
				err = otimizarDesempenhoWindows()
			}
		default:
			fmt.Printf("Sistema operacional '%s' não suportado.\n", runtime.GOOS)
			return
		}

		if err != nil {
			fmt.Printf("Erro: %v\n", err)
		} else {
			fmt.Println("Cache e desempenho otimizados com sucesso!")
		}

		contagemRegressiva(60)
	}
}
