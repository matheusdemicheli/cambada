import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  autor: any;
  data: any;
  texto: any;

  constructor(public navCtrl: NavController, public http: Http) {

    this.http.get('http://localhost:8000/frase_historica_aleatoria/').map(res => res.json()).subscribe(data => {
        this.autor = data.autor;
        this.data = data.data;
        this.texto = data.texto;
    });
  }

}
