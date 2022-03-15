import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm : FormGroup;
  hide : boolean = true;

  constructor(private fb : FormBuilder, private router : Router) {
    this.loginForm = fb.group({
      username : ['', Validators.required],
      password : ['', Validators.required]
    })
  }

  ngOnInit(): void {
  }

  sendUser(){
    const user = {
      username : this.loginForm.value.username,
      password : this.loginForm.value.password
    }
    this.router.navigate(['/principal'])
  }
}
