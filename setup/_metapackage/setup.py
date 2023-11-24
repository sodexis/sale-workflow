import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-partner_contact_sale_info_propagation>=16.0dev,<16.1dev',
        'odoo-addon-partner_sale_pivot>=16.0dev,<16.1dev',
        'odoo-addon-portal_sale_personal_data_only>=16.0dev,<16.1dev',
        'odoo-addon-product_form_sale_link>=16.0dev,<16.1dev',
        'odoo-addon-product_supplierinfo_for_customer_sale>=16.0dev,<16.1dev',
        'odoo-addon-sale_automatic_workflow>=16.0dev,<16.1dev',
        'odoo-addon-sale_automatic_workflow_job>=16.0dev,<16.1dev',
        'odoo-addon-sale_automatic_workflow_payment_mode>=16.0dev,<16.1dev',
        'odoo-addon-sale_cancel_reason>=16.0dev,<16.1dev',
        'odoo-addon-sale_commercial_partner>=16.0dev,<16.1dev',
        'odoo-addon-sale_company_currency>=16.0dev,<16.1dev',
        'odoo-addon-sale_delivery_split_date>=16.0dev,<16.1dev',
        'odoo-addon-sale_delivery_state>=16.0dev,<16.1dev',
        'odoo-addon-sale_discount_display_amount>=16.0dev,<16.1dev',
        'odoo-addon-sale_elaboration>=16.0dev,<16.1dev',
        'odoo-addon-sale_exception>=16.0dev,<16.1dev',
        'odoo-addon-sale_exception_holidays_public>=16.0dev,<16.1dev',
        'odoo-addon-sale_fixed_discount>=16.0dev,<16.1dev',
        'odoo-addon-sale_force_invoiced>=16.0dev,<16.1dev',
        'odoo-addon-sale_invoice_frequency>=16.0dev,<16.1dev',
        'odoo-addon-sale_manual_delivery>=16.0dev,<16.1dev',
        'odoo-addon-sale_mrp_bom>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_archive>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_currency_rate>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_general_discount>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_general_discount_triple>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_invoice_amount>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_invoicing_finished_task>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_line_date>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_line_delivery_state>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_line_menu>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_line_price_history>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_line_sequence>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_lot_generator>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_lot_selection>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_product_availability_inline>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_product_picker>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_product_recommendation>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_product_recommendation_packaging_default>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_qty_change_no_recompute>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_revision>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_type>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_warn_message>=16.0dev,<16.1dev',
        'odoo-addon-sale_packaging_default>=16.0dev,<16.1dev',
        'odoo-addon-sale_partner_incoterm>=16.0dev,<16.1dev',
        'odoo-addon-sale_partner_selectable_option>=16.0dev,<16.1dev',
        'odoo-addon-sale_payment_sheet>=16.0dev,<16.1dev',
        'odoo-addon-sale_pricelist_from_commitment_date>=16.0dev,<16.1dev',
        'odoo-addon-sale_procurement_group_by_line>=16.0dev,<16.1dev',
        'odoo-addon-sale_product_category_menu>=16.0dev,<16.1dev',
        'odoo-addon-sale_product_multi_add>=16.0dev,<16.1dev',
        'odoo-addon-sale_product_packaging_container_deposit>=16.0dev,<16.1dev',
        'odoo-addon-sale_product_set>=16.0dev,<16.1dev',
        'odoo-addon-sale_quotation_number>=16.0dev,<16.1dev',
        'odoo-addon-sale_start_end_dates>=16.0dev,<16.1dev',
        'odoo-addon-sale_stock_cancel_restriction>=16.0dev,<16.1dev',
        'odoo-addon-sale_stock_delivery_state>=16.0dev,<16.1dev',
        'odoo-addon-sale_stock_line_sequence>=16.0dev,<16.1dev',
        'odoo-addon-sale_stock_picking_blocking>=16.0dev,<16.1dev',
        'odoo-addon-sale_stock_picking_note>=16.0dev,<16.1dev',
        'odoo-addon-sale_substate>=16.0dev,<16.1dev',
        'odoo-addon-sale_tier_validation>=16.0dev,<16.1dev',
        'odoo-addon-sale_triple_discount>=16.0dev,<16.1dev',
        'odoo-addon-sale_wishlist>=16.0dev,<16.1dev',
        'odoo-addon-sales_team_security>=16.0dev,<16.1dev',
        'odoo-addon-sell_only_by_packaging>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
