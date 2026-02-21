"use client";

import { useCallback, useEffect, useState } from "react";
import {
  CATEGORIES,
  type Category,
  type Expense,
  type ExpenseInput,
} from "../lib/types";
import { loadExpenses, saveExpenses } from "../lib/storage";

const INITIAL_FORM: ExpenseInput = {
  date: new Date().toISOString().slice(0, 10),
  amount: 0,
  category: "Other",
  description: "",
};

function formatCurrency(amount: number): string {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  }).format(amount);
}

function generateId(): string {
  return `${Date.now()}-${Math.random().toString(36).slice(2, 9)}`;
}

export default function Home() {
  const [expenses, setExpenses] = useState<Expense[]>([]);
  const [hydrated, setHydrated] = useState(false);
  const [form, setForm] = useState<ExpenseInput>(INITIAL_FORM);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [search, setSearch] = useState("");
  const [filterCategory, setFilterCategory] = useState<Category | "">("");
  const [dateFrom, setDateFrom] = useState("");
  const [dateTo, setDateTo] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  useEffect(() => {
    setExpenses(loadExpenses());
    setHydrated(true);
  }, []);

  useEffect(() => {
    if (hydrated) saveExpenses(expenses);
  }, [hydrated, expenses]);

  const validate = useCallback((): boolean => {
    const next: Record<string, string> = {};
    if (!form.date) next.date = "Date is required";
    if (form.amount <= 0 || Number.isNaN(form.amount))
      next.amount = "Amount must be greater than 0";
    if (!form.description.trim()) next.description = "Description is required";
    setErrors(next);
    return Object.keys(next).length === 0;
  }, [form]);

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      if (!validate()) return;
      if (editingId) {
        setExpenses((prev) =>
          prev.map((ex) =>
            ex.id === editingId
              ? { ...ex, ...form, createdAt: ex.createdAt }
              : ex
          )
        );
        setEditingId(null);
        setSuccessMessage("Expense updated.");
      } else {
        setExpenses((prev) => [
          ...prev,
          { ...form, id: generateId(), createdAt: Date.now() },
        ]);
        setSuccessMessage("Expense added.");
      }
      setForm(INITIAL_FORM);
      setForm((f) => ({ ...f, date: new Date().toISOString().slice(0, 10) }));
      setTimeout(() => setSuccessMessage(""), 2000);
    },
    [form, validate, editingId]
  );

  const handleEdit = useCallback((ex: Expense) => {
    setForm({
      date: ex.date,
      amount: ex.amount,
      category: ex.category,
      description: ex.description,
    });
    setEditingId(ex.id);
    setSuccessMessage("");
  }, []);

  const handleDelete = useCallback((id: string) => {
    setExpenses((prev) => prev.filter((ex) => ex.id !== id));
    if (editingId === id) {
      setEditingId(null);
      setForm(INITIAL_FORM);
    }
    setSuccessMessage("Expense deleted.");
    setTimeout(() => setSuccessMessage(""), 2000);
  }, [editingId]);

  const handleCancelEdit = useCallback(() => {
    setEditingId(null);
    setForm(INITIAL_FORM);
    setForm((f) => ({ ...f, date: new Date().toISOString().slice(0, 10) }));
    setErrors({});
  }, []);

  const filtered = expenses.filter((ex) => {
    if (search && !ex.description.toLowerCase().includes(search.toLowerCase()))
      return false;
    if (filterCategory && ex.category !== filterCategory) return false;
    if (dateFrom && ex.date < dateFrom) return false;
    if (dateTo && ex.date > dateTo) return false;
    return true;
  });

  const totalSpending = filtered.reduce((s, ex) => s + ex.amount, 0);
  const thisMonth = new Date().toISOString().slice(0, 7);
  const monthlySpending = filtered.reduce(
    (s, ex) => (ex.date.startsWith(thisMonth) ? s + ex.amount : s),
    0
  );
  const byCategory = CATEGORIES.map((cat) => ({
    category: cat,
    total: filtered.reduce((s, ex) => (ex.category === cat ? s + ex.amount : s), 0),
  })).filter((x) => x.total > 0);
  const maxCategoryTotal = Math.max(1, ...byCategory.map((x) => x.total));

  const exportCSV = useCallback(() => {
    const headers = "Date,Amount,Category,Description\n";
    const rows = expenses
      .map(
        (ex) =>
          `${ex.date},${ex.amount},"${ex.category}","${ex.description.replace(/"/g, '""')}"`
      )
      .join("\n");
    const blob = new Blob([headers + rows], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `expenses-${new Date().toISOString().slice(0, 10)}.csv`;
    a.click();
    URL.revokeObjectURL(url);
    setSuccessMessage("CSV exported.");
    setTimeout(() => setSuccessMessage(""), 2000);
  }, [expenses]);

  if (!hydrated) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <p className="text-slate-600">Loading...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="bg-white border-b border-slate-200 shadow-sm">
        <div className="max-w-5xl mx-auto px-4 py-5">
          <h1 className="text-2xl font-bold text-slate-800">
            Expense Tracker
          </h1>
          <p className="text-slate-600 text-sm mt-1">
            Track and manage your personal expenses
          </p>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 py-6 space-y-6">
        {successMessage && (
          <div
            role="alert"
            className="bg-emerald-100 text-emerald-800 px-4 py-2 rounded-lg text-sm"
          >
            {successMessage}
          </div>
        )}

        {/* Form */}
        <section className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
          <h2 className="text-lg font-semibold text-slate-800 mb-4">
            {editingId ? "Edit expense" : "Add expense"}
          </h2>
          <form onSubmit={handleSubmit} className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">
                Date
              </label>
              <input
                type="date"
                value={form.date}
                onChange={(e) => setForm((f) => ({ ...f, date: e.target.value }))}
                className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
              {errors.date && (
                <p className="text-red-600 text-xs mt-1">{errors.date}</p>
              )}
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">
                Amount ($)
              </label>
              <input
                type="number"
                min="0"
                step="0.01"
                value={form.amount || ""}
                onChange={(e) =>
                  setForm((f) => ({ ...f, amount: parseFloat(e.target.value) || 0 }))
                }
                className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
              {errors.amount && (
                <p className="text-red-600 text-xs mt-1">{errors.amount}</p>
              )}
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">
                Category
              </label>
              <select
                value={form.category}
                onChange={(e) =>
                  setForm((f) => ({ ...f, category: e.target.value as Category }))
                }
                className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              >
                {CATEGORIES.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>
            <div className="sm:col-span-2 lg:col-span-1 flex flex-col justify-end gap-2 sm:flex-row lg:flex-col">
              <div className="flex-1 min-w-0">
                <label className="block text-sm font-medium text-slate-700 mb-1">
                  Description
                </label>
                <input
                  type="text"
                  value={form.description}
                  onChange={(e) =>
                    setForm((f) => ({ ...f, description: e.target.value }))
                  }
                  placeholder="e.g. Groceries"
                  className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                />
                {errors.description && (
                  <p className="text-red-600 text-xs mt-1">{errors.description}</p>
                )}
              </div>
              <div className="flex gap-2">
                <button
                  type="submit"
                  className="px-4 py-2 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
                >
                  {editingId ? "Update" : "Add"}
                </button>
                {editingId && (
                  <button
                    type="button"
                    onClick={handleCancelEdit}
                    className="px-4 py-2 bg-slate-200 text-slate-700 rounded-lg font-medium hover:bg-slate-300"
                  >
                    Cancel
                  </button>
                )}
              </div>
            </div>
          </form>
        </section>

        {/* Summary cards */}
        <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
            <p className="text-slate-600 text-sm font-medium">Total (filtered)</p>
            <p className="text-2xl font-bold text-slate-900 mt-1">
              {formatCurrency(totalSpending)}
            </p>
          </div>
          <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
            <p className="text-slate-600 text-sm font-medium">This month</p>
            <p className="text-2xl font-bold text-slate-900 mt-1">
              {formatCurrency(monthlySpending)}
            </p>
          </div>
          <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 sm:col-span-2 lg:col-span-1">
            <p className="text-slate-600 text-sm font-medium">Top categories</p>
            <ul className="mt-2 space-y-1 text-sm text-slate-800">
              {byCategory
                .sort((a, b) => b.total - a.total)
                .slice(0, 3)
                .map(({ category, total }) => (
                  <li key={category}>
                    {category}: {formatCurrency(total)}
                  </li>
                ))}
              {byCategory.length === 0 && (
                <li className="text-slate-500">No data yet</li>
              )}
            </ul>
          </div>
        </section>

        {/* Simple bar chart */}
        {byCategory.length > 0 && (
          <section className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
            <h2 className="text-lg font-semibold text-slate-800 mb-4">
              Spending by category
            </h2>
            <div className="space-y-3">
              {byCategory
                .sort((a, b) => b.total - a.total)
                .map(({ category, total }) => (
                  <div key={category} className="flex items-center gap-3">
                    <span className="w-28 text-sm text-slate-700 shrink-0">
                      {category}
                    </span>
                    <div className="flex-1 h-6 bg-slate-100 rounded overflow-hidden">
                      <div
                        className="h-full bg-blue-500 rounded transition-all duration-300"
                        style={{
                          width: `${(total / maxCategoryTotal) * 100}%`,
                        }}
                      />
                    </div>
                    <span className="text-sm font-medium text-slate-800 w-20 text-right">
                      {formatCurrency(total)}
                    </span>
                  </div>
                ))}
            </div>
          </section>
        )}

        {/* Filters and export */}
        <section className="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
          <div className="flex flex-wrap items-end gap-4">
            <div className="min-w-[180px]">
              <label className="block text-sm font-medium text-slate-700 mb-1">
                Search
              </label>
              <input
                type="text"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                placeholder="Description..."
                className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div className="min-w-[140px]">
              <label className="block text-sm font-medium text-slate-700 mb-1">
                Category
              </label>
              <select
                value={filterCategory}
                onChange={(e) =>
                  setFilterCategory(e.target.value as Category | "")
                }
                className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500"
              >
                <option value="">All</option>
                {CATEGORIES.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>
            <div className="min-w-[140px]">
              <label className="block text-sm font-medium text-slate-700 mb-1">
                From date
              </label>
              <input
                type="date"
                value={dateFrom}
                onChange={(e) => setDateFrom(e.target.value)}
                className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div className="min-w-[140px]">
              <label className="block text-sm font-medium text-slate-700 mb-1">
                To date
              </label>
              <input
                type="date"
                value={dateTo}
                onChange={(e) => setDateTo(e.target.value)}
                className="w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <button
              type="button"
              onClick={exportCSV}
              className="px-4 py-2 bg-slate-700 text-white rounded-lg font-medium hover:bg-slate-800 focus:ring-2 focus:ring-slate-500"
            >
              Export CSV
            </button>
          </div>
        </section>

        {/* Expense list */}
        <section className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
          <h2 className="text-lg font-semibold text-slate-800 p-5 pb-0">
            Expenses
          </h2>
          <div className="overflow-x-auto">
            <table className="w-full text-left">
              <thead>
                <tr className="border-b border-slate-200 bg-slate-50 text-slate-600 text-sm">
                  <th className="px-5 py-3 font-medium">Date</th>
                  <th className="px-5 py-3 font-medium">Amount</th>
                  <th className="px-5 py-3 font-medium">Category</th>
                  <th className="px-5 py-3 font-medium">Description</th>
                  <th className="px-5 py-3 font-medium w-24">Actions</th>
                </tr>
              </thead>
              <tbody>
                {filtered.length === 0 ? (
                  <tr>
                    <td colSpan={5} className="px-5 py-8 text-center text-slate-500">
                      No expenses match your filters. Add one above or clear filters.
                    </td>
                  </tr>
                ) : (
                  filtered.map((ex) => (
                    <tr
                      key={ex.id}
                      className="border-b border-slate-100 hover:bg-slate-50/50"
                    >
                      <td className="px-5 py-3 text-slate-800">{ex.date}</td>
                      <td className="px-5 py-3 font-medium text-slate-900">
                        {formatCurrency(ex.amount)}
                      </td>
                      <td className="px-5 py-3 text-slate-700">{ex.category}</td>
                      <td className="px-5 py-3 text-slate-700">
                        {ex.description}
                      </td>
                      <td className="px-5 py-3">
                        <div className="flex gap-2">
                          <button
                            type="button"
                            onClick={() => handleEdit(ex)}
                            className="text-blue-600 hover:underline text-sm"
                          >
                            Edit
                          </button>
                          <button
                            type="button"
                            onClick={() => handleDelete(ex.id)}
                            className="text-red-600 hover:underline text-sm"
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  );
}
