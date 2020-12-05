<template>
    <v-navigation-drawer app right v-model="open" disable-resize-watcher>
        <v-list flat>
            <v-subheader class="font-weight-bold text-overline"
                >Finances</v-subheader
            >
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title>Current Balance</v-list-item-title>
                    <v-list-item-subtitle>
                        Current amount in your account
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                        Can be used for daily expenses, sudden monetary
                        obligations
                    </v-list-item-subtitle>
                    <v-chip outlined color="success" class="text-subtitle">
                        {{ current }}
                    </v-chip>
                </v-list-item-content>
            </v-list-item>
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title>Monthly expenses</v-list-item-title>
                    <v-list-item-subtitle>
                        Monthly cost of living
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                        This amount is deducted from your balance every month
                    </v-list-item-subtitle>
                    <v-chip outlined color="warning" class="text-subtitle">
                        {{ expenditure }}
                    </v-chip>
                </v-list-item-content>
            </v-list-item>
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title>Salary</v-list-item-title>
                    <v-list-item-subtitle>
                        Monthly income
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                        This amount is added to your balance every month
                    </v-list-item-subtitle>
                    <v-chip outlined color="info" class="text-subtitle">
                        {{ salary }}
                    </v-chip>
                </v-list-item-content>
            </v-list-item>
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title>Running Debt</v-list-item-title>
                    <v-list-item-subtitle>
                        Amount you owe
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                        This amount experiences a monthly interest rate (MPY
                        <strong class="text-subtitle"
                            >{{ rates.interest }}%</strong
                        >)
                    </v-list-item-subtitle>
                    <v-chip outlined color="error" class="text-subtitle">
                        {{ debt }}
                    </v-chip>
                </v-list-item-content>
            </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-list flat dense>
            <v-subheader class="font-weight-bold text-overline"
                >Actions</v-subheader
            >
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title>Pay Debt</v-list-item-title>
                    <v-list-item-subtitle> </v-list-item-subtitle>
                    <v-list-item-subtitle>
                        <v-btn
                            block
                            text
                            small
                            @click="payDebt"
                            color="error"
                            class="ma-0 pa-0"
                            >Current -> Debt</v-btn
                        >
                    </v-list-item-subtitle>
                    <v-text-field
                        flat
                        dense
                        v-model="transfer"
                        label="Amount"
                        rounded
                        outlined
                    ></v-text-field>
                </v-list-item-content>
            </v-list-item>
            <v-list-item three-line>
                <v-list-item-content>
                    <v-list-item-title>Take Loan</v-list-item-title>
                    <v-list-item-subtitle
                        >Apply for loan (APY
                        <strong class="text-subtitle">{{ rates.bank }}%</strong
                        >)</v-list-item-subtitle
                    >
                    <v-list-item-subtitle>
                        <v-btn
                            block
                            text
                            small
                            color="success"
                            @click="applyLoan"
                            class="ma-0 pa-0"
                            >Apply</v-btn
                        >
                    </v-list-item-subtitle>
                    <v-text-field
                        flat
                        dense
                        v-model="loanAmt"
                        label="Amount"
                        rounded
                        outlined
                    ></v-text-field>
                </v-list-item-content>
            </v-list-item>
        </v-list>
        <v-list flat dense>
            <v-subheader class="font-weight-bold text-overline"
                >Insurances</v-subheader
            >
            <v-list-item
                v-for="insurance in Object.keys(insurances)"
                :key="insurance"
            >
                <v-list-item-content>
                    <v-list-item-title>{{ insurance }}</v-list-item-title>
                    <v-checkbox
                        v-model="insurances[insurance]"
                        readonly
                        hide-details
                    ></v-checkbox>
                </v-list-item-content>
            </v-list-item>
        </v-list>
        <template v-slot:append>
            <div class="pa-2">
                <v-btn block>
                    <v-icon left>mdi-content-save</v-icon> Save Game</v-btn
                >
            </div>
        </template>
    </v-navigation-drawer>
</template>
<script>
import { mapState } from 'vuex';
import api from '../api/core';
export default {
    name: 'Finance',
    props: ['open'],
    data: () => ({
        loanAmt: 0,
        transfer: 0,
    }),
    computed: {
        ...mapState('finance', {
            current: state => state.costs.current,
            debt: state => state.costs.debt,
            expenditure: state => state.costs.expenditure,
            salary: state => state.costs.salary,
            rates: state => state.rates,
            insurances: state => state.insurances,
        }),
    },
    methods: {
        async payDebt() {
            if (
                this.debt &&
                this.transfer > 0 &&
                this.transfer <= this.current &&
                this.transfer <= this.debt
            ) {
                this.current -= this.transfer;
                this.debt -= this.transfer;
                let expenditure = this.expenditure,
                    salary = this.salary;
                await api
                    .updateCosts({
                        current: this.current,
                        debt: this.debt,
                        expenditure,
                        salary,
                        ...this.rates,
                    })
                    .then(newFin => {
                        this.$store.dispatch(
                            'finance/loadState',
                            newFin.finances
                        );
                        this.transfer = 0;
                    })
                    .catch(err => console.error(err));
            }
        },
        async applyLoan() {
            if (this.loanAmt > 0) {
                let current = this.current + this.loanAmt;
                let expenditure =
                        this.expenditure +
                        (this.loanAmt * (1 + this.rates.bank / 100)) /
                            (12 * 10),
                    salary = this.salary;
                await api
                    .updateCosts({
                        current,
                        debt: this.debt,
                        expenditure,
                        salary,
                        ...this.rates,
                    })
                    .then(newFin => {
                        this.$store.dispatch(
                            'finance/loadState',
                            newFin.finances
                        );
                        this.loanAmt = 0;
                    })
                    .catch(err => console.error(err));
            }
        },
    },
};
</script>