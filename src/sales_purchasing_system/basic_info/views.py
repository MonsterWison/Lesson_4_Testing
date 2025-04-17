from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from sqlmodel import Session, select
from ..models.customer import Customer, CustomerAddress
from .. import db
from datetime import datetime

basic_info_bp = Blueprint('basic_info', __name__)

@basic_info_bp.route('/')
@login_required
def index():
    return render_template('basic_info/index.html')

@basic_info_bp.route('/customers')
@login_required
def customer_list():
    with Session(db.engine) as session:
        customers = session.exec(select(Customer)).all()
    return render_template('basic_info/customers/list.html', customers=customers)

@basic_info_bp.route('/customers/create', methods=['GET', 'POST'])
@login_required
def customer_create():
    if request.method == 'POST':
        customer_data = request.form.to_dict()
        addresses_data = request.form.getlist('addresses[]')
        
        with Session(db.engine) as session:
            customer = Customer(
                customer_id=customer_data['customer_id'],
                short_name=customer_data['short_name'],
                long_name=customer_data['long_name'],
                contact_person=customer_data['contact_person'],
                contact_title=customer_data.get('contact_title'),
                contact_department=customer_data.get('contact_department'),
                telephone=customer_data['telephone'],
                fax=customer_data.get('fax'),
                email=customer_data.get('email'),
                website=customer_data.get('website'),
                payment_terms=customer_data['payment_terms'],
                memo=customer_data.get('memo'),
                last_modified_by=current_user.username
            )
            
            session.add(customer)
            session.commit()
            
            # Add addresses
            for addr_data in addresses_data:
                address = CustomerAddress(
                    customer_id=customer.id,
                    **addr_data
                )
                session.add(address)
            
            session.commit()
            flash('Customer created successfully', 'success')
            return redirect(url_for('basic_info.customer_list'))
    
    return render_template('basic_info/customers/create.html')

@basic_info_bp.route('/customers/<int:id>')
@login_required
def customer_detail(id):
    with Session(db.engine) as session:
        customer = session.get(Customer, id)
        if not customer:
            flash('Customer not found', 'error')
            return redirect(url_for('basic_info.customer_list'))
    return render_template('basic_info/customers/detail.html', customer=customer)

@basic_info_bp.route('/customers/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def customer_edit(id):
    with Session(db.engine) as session:
        customer = session.get(Customer, id)
        if not customer:
            flash('Customer not found', 'error')
            return redirect(url_for('basic_info.customer_list'))
        
        if request.method == 'POST':
            customer_data = request.form.to_dict()
            for key, value in customer_data.items():
                setattr(customer, key, value)
            customer.modified_at = datetime.utcnow()
            customer.last_modified_by = current_user.username
            
            session.commit()
            flash('Customer updated successfully', 'success')
            return redirect(url_for('basic_info.customer_detail', id=id))
    
    return render_template('basic_info/customers/edit.html', customer=customer)

@basic_info_bp.route('/customers/<int:id>/delete', methods=['POST'])
@login_required
def customer_delete(id):
    with Session(db.engine) as session:
        customer = session.get(Customer, id)
        if not customer:
            flash('Customer not found', 'error')
            return redirect(url_for('basic_info.customer_list'))
        
        session.delete(customer)
        session.commit()
        flash('Customer deleted successfully', 'success')
    return redirect(url_for('basic_info.customer_list')) 