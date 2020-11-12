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
                        {{ monthly }}
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
                        <strong class="text-subtitle">{{ rates.debt }}%</strong
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
                        <v-btn block text small color="error" class="ma-0 pa-0"
                            >Current -> Debt</v-btn
                        >
                    </v-list-item-subtitle>
                    <v-text-field
                        flat
                        dense
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
                        <strong class="text-subtitle">{{ rates.loan }}%</strong
                        >)</v-list-item-subtitle
                    >
                    <v-list-item-subtitle>
                        <v-btn
                            block
                            text
                            small
                            color="success"
                            class="ma-0 pa-0"
                            >Apply</v-btn
                        >
                    </v-list-item-subtitle>
                    <v-text-field
                        flat
                        dense
                        label="Amount"
                        rounded
                        outlined
                    ></v-text-field>
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
export default {
    name: 'Finance',
    props: ['open'],
    data: () => ({
        current: 20000,
        debt: -5000,
        monthly: 7400,
        rates: {
            debt: 4.5,
            loan: 6,
        },
    }),
};
</script>