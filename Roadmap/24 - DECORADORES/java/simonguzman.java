
import java.util.HashMap;
import java.util.Map;



public class simonguzman {
    public  static void main(String[] args) {
        genericExample();
        example();
    }

    /***************************** Ejemplo de implemetacion mas complejo *****************************/
    static void example(){
        UserService userService = new LoginAttemptsDecorator(new BasicUserService(), 3);
        userService.login("user1", "password");
        userService.login("user1", "wrongpassword");
        userService.login("user1", "wrongpassword");
        userService.login("user1", "wrongpassword");
        userService.login("user1", "wrongpassword");
    }
    static interface UserService{
        boolean login(String username, String password);
    }

    static class BasicUserService implements UserService{
        private Map<String, String> userDatabase = new HashMap<>();

        public BasicUserService(){
            userDatabase.put("user1", "password");
            userDatabase.put("user2", "12345");
        }

        @Override
        public boolean login(String username, String password){
            String storedPassword = userDatabase.get(username);
            if(storedPassword != null && storedPassword.equals(password)){
                System.out.println("Inicio de sesion exitoso para "+username);
                return true;
            }else{
                System.out.println("Credenciales incorrectas para "+username);
                return false;
            }
        }
    }

    static class LoginAttemptsDecorator implements UserService{
        private UserService userService;
        private Map<String, Integer> loginAttempts;
        private int maxAttempts;

        public LoginAttemptsDecorator(UserService userService, int maxAttempts) {
            this.userService = userService;
            this.maxAttempts = maxAttempts;
            this.loginAttempts = new HashMap<>();
        }

        @Override
        public boolean login(String username, String password) {
            if(loginAttempts.getOrDefault(username, 0) >= maxAttempts){
                System.out.println("Cuenta bloqueada para "+username+" por exceder los intentos permitidos");
                return false;
            }

            boolean success = userService.login(username, password);
            if(!success){
                loginAttempts.put(username, loginAttempts.getOrDefault(username, 0)+1);
                System.out.println("Intentos fallidos para "+username+":" + loginAttempts.get(username));
            }else{
                loginAttempts.put(username, 0);
            }
            return success;
        }
        
    }

    /***************************** Ejemplo generico *****************************/
    static void genericExample(){
        Component component = new ConcreteComponent();
        Component decorated = new ConcreteDecorator(component);
        decorated.operation();
    }
    
    //Interfaz base
    static interface Component{
        void operation();
    }

    //Componente concreto
    static class ConcreteComponent implements Component{
        @Override
        public void operation() {
            System.out.println("Ejecutando operacion base...");
        }
    }

    //Decorador abstracto
    static abstract class Decorator implements Component{
        protected Component component;

        public Decorator(Component component){
            this.component = component;
        }

        public void operation() {
            this.component.operation();
        }
    }

    //Decorador concreto que añade funcionalidad
    static class ConcreteDecorator extends Decorator{
        public ConcreteDecorator(Component component){
            super(component);
        }

        @Override
        public void operation() {
            super.operation();
            addFunctionality();
        }

        private void addFunctionality(){
            System.out.println("Funcionalidad adicional del decorador.");
        }
    }
}
