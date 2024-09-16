package application;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.MenuBar;
import javafx.scene.control.Label;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuItem;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
//Ricardo Armando Fuentes Arevalo 16/09/2024
public class Main extends Application {
    Stage primaryStage; //TOCÓ DECLARAR ESTE ATRIBUTO PARA USAR EL STAGE DESDE OTRA CLASE
    
    @Override
    public void start(Stage primaryStage) {
    	
        this.primaryStage = primaryStage;

        GridPane p1 = new GridPane();
        p1.setHgap(30);
        p1.add(new Label(" "), 0, 0);
        p1.add(new Label("Escena1"), 0, 1);
        
        BorderPane root = new BorderPane();
        
        MenuBar barraMenu = new MenuBar();
        Menu menu1 = new Menu("Opciones");
        barraMenu.getMenus().add(menu1);
        MenuItem Op1 = new MenuItem("Op1");
        menu1.getItems().add(Op1);
        root.setTop(barraMenu);
        root.setCenter(p1);
        
        boton1HandlerClass handler1 = new boton1HandlerClass();
        Op1.setOnAction(handler1);
        
     
        
        primaryStage.setTitle("Titulo");
        Scene scene = new Scene(root, 300, 300);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public void cambiarScene(Scene newScene) {
        primaryStage.setScene(newScene);
    }

    public static void main(String[] args) {
        launch(args);
    }

    //Clase para abrir la segunda ventana
    class boton1HandlerClass implements EventHandler<ActionEvent> {
 
        public void handle(ActionEvent e) {

        	GridPane p1 = new GridPane();
            p1.setHgap(30);
            p1.add(new Label(" "), 0, 0);
            p1.add(new Label("Escena2"), 0, 1);
            
            BorderPane root = new BorderPane();
            
            MenuBar barraMenu = new MenuBar();
            Menu menu1 = new Menu("Opciones");
            barraMenu.getMenus().add(menu1);
            MenuItem Op1 = new MenuItem("Op1");
            menu1.getItems().add(Op1);
            root.setTop(barraMenu);
            root.setCenter(p1);
            
            boton2HandlerClass handler2 = new boton2HandlerClass();
            Op1.setOnAction(handler2);

            Scene newScene = new Scene(root, 300, 300);
            cambiarScene(newScene);
        }
    }

 
    //Clase para abrir la primera ventana
    class boton2HandlerClass implements EventHandler<ActionEvent> {
    	
        public void handle(ActionEvent e) {

        	GridPane p1 = new GridPane();
            p1.setHgap(30);
            p1.add(new Label(" "), 0, 0);
            p1.add(new Label("Escena1"), 0, 1);
            
            BorderPane root = new BorderPane();
            
            MenuBar barraMenu = new MenuBar();
            Menu menu1 = new Menu("Opciones");
            barraMenu.getMenus().add(menu1);
            MenuItem Op1 = new MenuItem("Op1");
            menu1.getItems().add(Op1);
            root.setTop(barraMenu);
            root.setCenter(p1);

            boton1HandlerClass handler1 = new boton1HandlerClass();
            Op1.setOnAction(handler1);

            Scene newScene = new Scene(root, 300, 300);
            cambiarScene(newScene);
        }
    }
}