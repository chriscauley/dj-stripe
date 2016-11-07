# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djstripe.fields
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0017_set_null_on_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='account',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='charge',
            name='account',
            field=models.ForeignKey(related_name='charges', to='djstripe.Account', help_text='The account the charge was made on behalf of. Null here indicates that this value was never set.', null=True),
        ),
        migrations.AlterField(
            model_name='charge',
            name='amount_refunded',
            field=djstripe.fields.StripeCurrencyField(help_text=b'Amount refunded (can be less than the amount attribute on the charge if a partial refund was issued).', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='charge',
            name='captured',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'If the charge was created without capturing, this boolean represents whether or not it is still uncaptured or has since been captured.'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='currency',
            field=djstripe.fields.StripeCharField(help_text=b'Three-letter ISO currency code representing the currency in which the charge was made.', max_length=3),
        ),
        migrations.AlterField(
            model_name='charge',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='charge',
            name='paid',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'True if the charge succeeded, or was successfully authorized for later capture, False otherwise.'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='refunded',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'Whether or not the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='source_type',
            field=djstripe.fields.StripeCharField(help_text=b'The payment source type. If the payment source is supported by dj-stripe, a corresponding model is attached to this Charge via a foreign key matching this field.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charge',
            name='statement_descriptor',
            field=djstripe.fields.StripeCharField(help_text=b'An arbitrary string to be displayed on your customer\'s credit card statement. The statement description may not include <>"\' characters, and will appear on your customer\'s statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all.', max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='charge',
            name='transfer',
            field=models.ForeignKey(to='djstripe.Transfer', help_text='The transfer to the destination account (only applicable if the charge was created using the destination parameter).', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='account_balance',
            field=djstripe.fields.StripeIntegerField(help_text=b"Current balance, if any, being stored on the customer's account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring charges.", null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='currency',
            field=djstripe.fields.StripeCharField(help_text=b'The currency the customer can be charged in for recurring billing purposes (subscriptions, invoices, invoice items).', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='processed',
            field=models.BooleanField(default=False, help_text='If validity is performed, webhook event processor(s) may run to take further action on the event. Once these have run, this is set to True.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='received_api_version',
            field=djstripe.fields.StripeCharField(help_text=b'the API version at which the event data was rendered. Blank for old entries only, all new entries will have this value', max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='request_id',
            field=djstripe.fields.StripeCharField(help_text=b"Information about the request that triggered this event, for traceability purposes. If empty string then this is an old entry without that data. If Null then this is not an old entry, but a Stripe 'automated' event with no associated request.", max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='valid',
            field=models.NullBooleanField(help_text='Tri-state bool. Null == validity not yet confirmed. Otherwise, this field indicates that this event was checked via stripe api and found to be either authentic (valid=True) or in-authentic (possibly malicious)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='webhook_message',
            field=djstripe.fields.StripeJSONField(help_text=b'data received at webhook. data should be considered to be garbage until validity check is run and valid flag is set'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_due',
            field=djstripe.fields.StripeCurrencyField(help_text=b"Final amount due at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the amount_due may be 0. If there is a positive starting_balance for the invoice (the customer owes money), the amount_due will also take that into account. The charge that gets generated for the invoice will be for the amount specified in amount_due.", max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='application_fee',
            field=djstripe.fields.StripeCurrencyField(help_text=b"The fee in cents that will be applied to the invoice and transferred to the application owner's Stripe account when the invoice is paid.", null=True, max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='attempt_count',
            field=djstripe.fields.StripeIntegerField(help_text=b'Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='attempted',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'Whether or not an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the ``invoice.created`` webhook, for example, so you might not want to display that invoice as unpaid to your users.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='closed',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b"Whether or not the invoice is still trying to collect payment. An invoice is closed if it's either paid or it has been marked closed. A closed invoice will no longer attempt to collect payment."),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ending_balance',
            field=djstripe.fields.StripeIntegerField(help_text=b'Ending customer balance after attempting to pay invoice. If the invoice has not been attempted yet, this will be null.', null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='forgiven',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'Whether or not the invoice has been forgiven. Forgiving an invoice instructs us to update the subscription status as if the invoice were successfully paid. Once an invoice has been forgiven, it cannot be unforgiven or reopened.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='starting_balance',
            field=djstripe.fields.StripeIntegerField(help_text=b'Starting customer balance before attempting to pay invoice. If the invoice has not been attempted yet, this will be the current customer balance.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='statement_descriptor',
            field=djstripe.fields.StripeCharField(help_text=b'An arbitrary string to be displayed on your customer\'s credit card statement. The statement description may not include <>"\' characters, and will appear on your customer\'s statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all.', max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscription_proration_date',
            field=djstripe.fields.StripeDateTimeField(help_text=b'Only set for upcoming invoices that preview prorations. The time used to calculate prorations.', null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subtotal',
            field=djstripe.fields.StripeCurrencyField(help_text=b'Only set for upcoming invoices that preview prorations. The time used to calculate prorations.', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax',
            field=djstripe.fields.StripeCurrencyField(help_text=b'The amount of tax included in the total, calculated from ``tax_percent`` and the subtotal. If no ``tax_percent`` is defined, this value will be null.', null=True, max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax_percent',
            field=djstripe.fields.StripePercentField(help_text=b"This percentage of the subtotal has been added to the total amount of the invoice, including invoice line items and discounts. This field is inherited from the subscription's ``tax_percent`` field, but can be changed before the invoice is paid. This field defaults to null.", null=True, max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='discountable',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'If True, discounts will apply to this invoice item. Always False for prorations.'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='plan',
            field=models.ForeignKey(related_name='invoiceitems', on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Plan', help_text='If the invoice item is a proration, the plan of the subscription for which the proration was computed.', null=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='proration',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'Whether or not the invoice item was created automatically as a proration adjustment when the customer switched plans.'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='quantity',
            field=djstripe.fields.StripeIntegerField(help_text=b'If the invoice item is a proration, the quantity of the subscription for which the proration was computed.', null=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='subscription',
            field=models.ForeignKey(related_name='invoiceitems', on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Subscription', help_text='The subscription that this invoice item has been created for, if any.', null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='interval_count',
            field=djstripe.fields.StripeIntegerField(help_text=b'The number of intervals (specified in the interval property) between each subscription billing.', null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='statement_descriptor',
            field=djstripe.fields.StripeCharField(help_text=b'An arbitrary string to be displayed on your customer\'s credit card statement. The statement description may not include <>"\' characters, and will appear on your customer\'s statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all.', max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='trial_period_days',
            field=djstripe.fields.StripeIntegerField(help_text=b'Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period.', null=True),
        ),
        migrations.AlterField(
            model_name='stripesource',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='stripesource',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='application_fee_percent',
            field=djstripe.fields.StripePercentField(help_text=b'A positive decimal that represents the fee percentage of the subscription invoice amount that will be transferred to the application owner\xe2\x80\x99s Stripe account each billing period.', null=True, max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='cancel_at_period_end',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'If the subscription has been canceled with the ``at_period_end`` flag set to true, ``cancel_at_period_end`` on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period.'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='canceled_at',
            field=djstripe.fields.StripeDateTimeField(help_text=b'If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with ``cancel_at_period_end``, canceled_at will still reflect the date of the initial cancellation request, not the end of the subscription period when the subscription is automatically moved to a canceled state.', null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='current_period_end',
            field=djstripe.fields.StripeDateTimeField(help_text=b'End of the current period for which the subscription has been invoiced. At the end of this period, a new invoice will be created.'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='ended_at',
            field=djstripe.fields.StripeDateTimeField(help_text=b'If the subscription has ended (either because it was canceled or because the customer was switched to a subscription to a new plan), the date the subscription ended.', null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='tax_percent',
            field=djstripe.fields.StripePercentField(help_text=b'A positive decimal (with at most two decimal places) between 1 and 100. This represents the percentage of the subscription invoice subtotal that will be calculated and added as tax to the final amount each billing period.', null=True, max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='amount_reversed',
            field=djstripe.fields.StripeCurrencyField(help_text=b'The amount reversed (can be less than the amount attribute on the transfer if a partial reversal was issued).', null=True, max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='date',
            field=djstripe.fields.StripeDateTimeField(help_text=b"Date the transfer is scheduled to arrive in the bank. This doesn't factor in delays like weekends or bank holidays."),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='destination',
            field=djstripe.fields.StripeIdField(help_text=b'ID of the bank account, card, or Stripe account the transfer was sent to.', max_length=255),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='destination_payment',
            field=djstripe.fields.StripeIdField(help_text=b'If the destination is a Stripe account, this will be the ID of the payment that the destination account received for the transfer.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='failure_code',
            field=djstripe.fields.StripeCharField(help_text=b'Error code explaining reason for transfer failure if available. See https://stripe.com/docs/api/python#transfer_failures.', max_length=23, null=True, choices=[(b'insufficient_funds', b'Insufficient Funds'), (b'account_closed', b'Account Closed'), (b'no_account', b'No Account'), (b'invalid_account_number', b'Invalid Account Number'), (b'debit_not_authorized', b'Debit Not Authorized'), (b'bank_ownership_changed', b'Bank Ownership Changed'), (b'account_frozen', b'Account Frozen'), (b'could_not_process', b'Could Not Process'), (b'bank_account_restricted', b'Bank Account Restricted'), (b'invalid_currency', b'Invalid Currency')]),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='livemode',
            field=djstripe.fields.StripeNullBooleanField(default=False, help_text=b'Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='metadata',
            field=djstripe.fields.StripeJSONField(help_text=b'A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='reversed',
            field=djstripe.fields.StripeBooleanField(default=False, help_text=b'Whether or not the transfer has been fully reversed. If the transfer is only partially reversed, this attribute will still be false.'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='source_transaction',
            field=djstripe.fields.StripeIdField(help_text=b'ID of the charge (or other transaction) that was used to fund the transfer. If null, the transfer was funded from the available balance.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='statement_descriptor',
            field=djstripe.fields.StripeCharField(help_text=b'An arbitrary string to be displayed on your customer\'s credit card statement. The statement description may not include <>"\' characters, and will appear on your customer\'s statement in capital letters. Non-ASCII characters are automatically stripped. While most banks display this information consistently, some may display it incorrectly or not at all.', max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='status',
            field=djstripe.fields.StripeCharField(help_text=b'The current status of the transfer. A transfer will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.', max_length=10, choices=[(b'paid', b'Paid'), (b'pending', b'Pending'), (b'in_transit', b'In Transit'), (b'canceled', b'Canceled'), (b'failed', b'Failed')]),
        ),
    ]
