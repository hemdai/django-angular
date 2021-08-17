import { Component, OnInit, Input } from '@angular/core';
import { SharedService } from 'src/app/shared.service';


@Component({
  selector: 'app-show-dept',
  templateUrl: './show-dept.component.html',
  styleUrls: ['./show-dept.component.css']
})
export class ShowDeptComponent implements OnInit {

  constructor(private service:SharedService) { }

  DepartmentList: any = [];

  ModalTitle: string="";
  ActivateAddEditDepComp: boolean = false;
  dep: any="";

  ngOnInit(): void {
    this.refreshDepList();
  }

  addClick() {
    this.dep = {
      id:0,
      name:""
    }
    this.ModalTitle = "AddDepartment";
    this.ActivateAddEditDepComp = true;
    
  }

  closeClick() {
    this.ActivateAddEditDepComp = false;
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getDepList().subscribe(data => {
      this.DepartmentList = data;
    })
  }

}
