/*
 * Basicamente, o programa tem um loop infinito que executa a função que cria uma lista de palavras e a cada
 * 4 segundos imprime a palavra. Ja a classe ThreadSimples aguarda que outra thread termine sua execução e verifica a cada 1 segundo se a 
 * execução da thread Loop finalize
 * 
 * 
 */



public class ThreadSimples {
    static void mensagem(String messagem) { //declaração da interface do método
        String nomeThread = Thread.currentThread().getName(); //obtém da thread em execução
        System.out.println(nomeThread + " " + messagem); //printa o nome da thread concatenando com o parametro messagem recebido pelo método
    }
    private static class Loop implements Runnable { //declaração da classe implementando a interface Runnable
        public void run() { // declaração do método run que deve ser implementando por conta da interface Runnable
            String info[] = { // Declaração de um array de strings chamado info
                    "Java",
                    "é uma boa linguagem.",
                    "Com threads,",
                    "é melhor ainda."
            };
            try { //Abre um bloco try/catch
                for (int i = 0; i < info.length; i++) { // declaração inicial de um laço de repetição que executará 4 vezes (numero de elementos do array info)
                    Thread.sleep(4000); // Coloca a thread em estado de sleep por 4000ms
                    mensagem(info[i]); // Invoca o método mensagem com o item está posição i do array info
                }
            } catch (InterruptedException e) { // captura uma exceção lançada do tipo InterruptedException
                mensagem("Nada feito!"); // Invoca o método mensagem com a string "Nada feito!"
            }
        }
    }
  
    public static void main(String args[]) throws InterruptedException { // Declaração da assinatura do método main e indica a classe pode lançar uma InterruptedException
        long paciencia = 1000 * 60 * 60; // inicializa uma variável pacienca com o valor da operação aritmética 1000 * 60 * 60
        if (args.length > 0) { // bloco if verifica se o tamanho do array args recebido é maior que zero
            try { // abre um bloco try/catch
                paciencia = Long.parseLong(args[0]) * 1000; // multiplica por 1000 o valor da operação de arg 0
            } catch (NumberFormatException e) {// pega a excessao ao erro
                System.err.println("Argumento deve ser um inteiro.");// printa no terminal mensagem de erro
                System.exit(1);// encerra o programa
            }
        }
        mensagem("Iniciando a thread Loop");
        long inicio = System.currentTimeMillis();// pega o tempo atual em milissegundos
        Thread t = new Thread(new Loop());// Inicia uma thread com a classe loop
        t.start();// inicia a thread
        mensagem("Esperando que a thread Loop termine");// fala para o usuário que a thread começou
        while (t.isAlive()) {// Condição para verificar enquanto a thread está viva
            mensagem("Ainda esperando...");// printa para o usuário um aviso
            t.join(1000);// espera 1 segundo para finalizar a thread
            if (((System.currentTimeMillis() - inicio) > paciencia) && // verifica se o tempo atual menos o tempo de inicio da thread é maior que variavel paciencia e se thread esta viva
                    t.isAlive()) {
                mensagem("Cansado de esperar!");// mostra mensagem para o usuário
                t.interrupt();// para a thread
                t.join(); // Espera a thread terminar pra continuar executando
            }
        }
        mensagem("Finalmente!");
    }
  }