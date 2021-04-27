import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderinicioComponent } from './headerinicio.component';

describe('HeaderinicioComponent', () => {
  let component: HeaderinicioComponent;
  let fixture: ComponentFixture<HeaderinicioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HeaderinicioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HeaderinicioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
